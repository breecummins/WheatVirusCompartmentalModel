# using Plots

type SquareMatrix
    matrix::Array{Float64,2}
    dim::Int
    SquareMatrix(matrix,dim) = size(matrix)[1] != size(matrix)[2] ? error("non-square matrix") : new(matrix,size(matrix)[1])
end
SquareMatrix(X) = SquareMatrix(X,size(X)[1])

type Proportion
    prop::Float64
    Proportion(prop) = !(0 <= prop <= 1) ? error("not a proportion") : new(prop)
end

type ClimateParameter
    VWpop::Int
    time_periods::Array{Float64}
    beta5::Proportion
    tau1::Float64
    low_gamma2::Proportion
    high_gamma2::Proportion
end

type Parameter
    population::Array{Int}
    beta::SquareMatrix
    climate::ClimateParameter
    Cnminus1::Int
    tau2::Float64
    tau3::Proportion
    gamma11::Proportion
    gamma13::Proportion
end

function forwardEuler(A::SquareMatrix,param::Parameter,icv::Array{Float64,1},rows::Array{Int,1},time_per::Float64,numsteps::Int)
    # limits numerical error as compared to forwardMap
    timestep = time_per/numsteps
    while numsteps >0
        # perform forward mapping of initial conditions icv on populations pop restricted to indices in rows
        B = A.matrix .* (1 - icv) / sum(param.population[rows])
        # zero out entries that are not in rows
        rem = filter(x -> !(x in rows), 1:A.dim) 
        B[:,rem] = B[rem,:] = 0
        # forward Euler
        icv = (eye(A.dim) + timestep*B)*icv
        numsteps -= 1
    end
    icv
end

function testsolver(numsteps=1000,climate=(climate_ambient,false))
    ICs = Float64[3.3e5,3.3e5,1e6,0.5] # Cn-1 pop, Cn pop, VWn pop, VWn prop infected
    populations = map((x) -> convert(Int,x),ICs[1:3])
    param = setparams(climate,populations)
    IC_virus = [0, ICs[4], 0, 0]
    A = SquareMatrix((param.beta.matrix) .* (param.population'))
    x0 = param.climate.time_periods[1]
    beta = param.beta.matrix[2,2]
    C = (1 - IC_virus[2]) / IC_virus[2]
    intVW = exp(beta * x0)  / (exp(beta * x0) + C)
    rows0 = [2]
    V0 = forwardEuler(A,param,IC_virus,rows0,x0,convert(Int,x0*numsteps))
    println("Exact soln, FE with $numsteps steps, Difference: \n$intVW, $(V0[2]), $(abs(intVW - V0[2]))")
end


function fullyear(param::Parameter,IC_virus::Array{Float64,1},steps_per_time::Int)
    # volunteer wheat only
    x0 = param.climate.time_periods[1]
    # construct V0 exactly instead of using forward Euler
    beta = param.beta.matrix[2,2]
    C = (1 - IC_virus[2]) / IC_virus[2]
    intVW = exp(beta * x0)  / (exp(beta * x0) + C)
    V0 = Float64[0, intVW, 0, 0]
    # construct transmission/population matrix A
    A = SquareMatrix((param.beta.matrix) .* (param.population'))
    # volunteer wheat -> wheat and cheatgrass
    # this is split into 3 different steps to record differing yield loss to infection
    rows1 = [1,2,3]
    x1 = param.climate.time_periods[2]
    V1 = forwardEuler(A,param,V0,rows1,x1,convert(Int,x1*steps_per_time))
    # growth period after hibernation
    x3 = param.climate.time_periods[3]
    V3 = forwardEuler(A,param,V1,rows1,x3,convert(Int,x3*steps_per_time))
    # plant growth has stopped and cheatgrass is still living
    x4 = param.climate.time_periods[4]
    V4 = forwardEuler(A,param,V3,rows1,x4,convert(Int,x4*steps_per_time))
    # wheat -> new volunteer wheat after cheatgrass death
    rows5 = [2,3,4]
    x5 = param.climate.time_periods[5]
    V5 = forwardEuler(A,param,V4,rows5,x5,convert(Int,x5*steps_per_time))
    (V1,V3,V5)
end

function multiyear(yearly_climates=Array{Tuple{Function,Bool},1}, ICs=Float64[]; steps_per_time=100)
    yearly_climates = reverse(yearly_climates) # julia pops from the back
    results = []
    while length(yearly_climates) > 0
        climate = pop!(yearly_climates)
        populations = map((x) -> convert(Int,x),ICs[1:3])
        param = setparams(climate,populations)
        IC_virus = [0, ICs[4], 0, 0]
        (V1,V3,V5) = fullyear(param,IC_virus,steps_per_time)
        (Cnplus1,Ynplus1) = wheat_yield(param,V1,V3,V5)
        append!(results,[(Cnplus1,Ynplus1,V5)])
        ICs = Float64[param.population[1],Cnplus1,param.climate.VWpop,V5[4]]
    end
    # results = [new cheatgrass, wheat yield, ending proportions infected (cheatgrass, volunteer wheat, wheat, new volunteer wheat)]
    results
end

function wheat_yield(param::Parameter,V1::Array{Float64,1},V3::Array{Float64,1},V5::Array{Float64,1})
    Cnplus1 = convert(Int,round(param.tau3.prop*( param.climate.tau1*param.population[1] + param.tau2*param.Cnminus1 )))
    gamma2 = param.population[1] <= 5e5 ? param.climate.low_gamma2.prop : param.climate.high_gamma2.prop #arbitrary threshold
    Ynplus1 = (1-gamma2)*( param.gamma11.prop*V1[3] + param.gamma13.prop*(V3[3] - V1[3]) + 1 - V3[3] ) 
    (Cnplus1,Ynplus1)
end

function setparams(climate::Tuple{Function,Bool},ICs::Array{Int,1})
    # ICs=Int[Cnminus1,Cn,VWpop]
    W = convert(Int,2.25e6) # 225 plants/m^2 in one hectare field
    Cnminus1 = ICs[1]
    climate_parameter = climate[1](W,climate[2])
    pop = Int[ICs[2], ICs[3], W, climate_parameter.VWpop]
    beta1=Proportion(0.00) # cheatgrass to cheatgrass (see Tim's email 10/25)
    beta2=Proportion(0.25) # wheat/volunteer wheat to cheatgrass
    beta3=Proportion(0.3) #cheatgrass to wheat/volunteer wheat
    beta4=Proportion(0.5) # wheat to wheat/volunteer wheat
    beta5= climate_parameter.beta5 # volunteer wheat to volunteer wheat
    # matrix order = [cheatgrass, volunteer wheat, wheat, new volunteer wheat]
    beta = SquareMatrix(Float64[
                         beta1.prop beta2.prop beta2.prop 0.0; 
                         beta3.prop beta5.prop beta4.prop 0.0;
                         beta3.prop beta4.prop beta4.prop 0.0;
                         0.0        beta4.prop beta4.prop 0.0;    
                         ])
    tau2 = 3.0 # can exceed 1 (cheatgrass plants per plant from previous year)
    tau3 = Proportion(0.1)  # free parameter (competition effect on cheatgrass from wheat)
    gamma11 = Proportion(0.7) # wheat yield given fall infection
    gamma13 = Proportion(0.85) # wheat yield given spring infection
    Parameter(pop,beta,climate_parameter,Cnminus1,tau2,tau3,gamma11,gamma13)
end

function climate_ambient(W,ishail=true)
    (VW,beta5) = hail(W,ishail)
    x0 = 3 # 3 time units = 6 weeks; these should change for hot and hot and dry climate scenarios, but I don't know how yet
    x1 = 2.5 
    x3 = 6
    x4 = 3 
    x5 = 1 
    time_periods = Float64[x0,x1,x3,x4,x5]
    tau1 = 6.0 #free parameter -- should be higher under hot conditions and higher yet under hot and dry conditions
    low_gamma2 = Proportion(0.34) 
    high_gamma2 = Proportion(0.40)
    ClimateParameter(VW, time_periods, beta5, tau1, low_gamma2, high_gamma2)
end

function climate_hot(W,ishail=true)
    (VW,beta5) = hail(W,ishail)
    x0 = 3 # 3 time units = 6 weeks; these should change for hot and hot and dry climate scenarios, but I don't know how yet
    x1 = 2.5 
    x3 = 6
    x4 = 3 
    x5 = 1 
    time_periods = Float64[x0,x1,x3,x4,x5]
    tau1 = 12.0 #free parameter -- should be higher yet under hot and dry conditions
    low_gamma2 = Proportion(0.33) 
    high_gamma2 = Proportion(0.38)
    ClimateParameter(VW, time_periods, beta5, tau1, low_gamma2, high_gamma2)
end

function climate_hotdry(W,ishail=true)
    (VW,beta5) = hail(W,ishail)
    x0 = 3 # 3 time units = 6 weeks; these should change for hot and hot and dry climate scenarios, but I don't know how yet
    x1 = 2.5 
    x3 = 6
    x4 = 3 
    x5 = 1 
    time_periods = Float64[x0,x1,x3,x4,x5]
    tau1 = 16.0 #free parameter -- should be higher than the other conditions
    low_gamma2 = Proportion(0.39) 
    high_gamma2 = Proportion(0.52)
    ClimateParameter(VW, time_periods, beta5, tau1, low_gamma2, high_gamma2)
end

function hail(W,ishail)
    # 100 plants/m^2 in one hectare field for hail, 10 for no hail
    VW = ishail ? convert(Int,1e6) : convert(Int,1e5)
    beta5 = Proportion(0.5 * VW / W) 
    (VW,beta5)
end

# # test the forward Euler solver
# testsolver(100)
# testsolver(250)
# testsolver(500)
# testsolver(750)
# testsolver(1000)

function hotdryyears(N,ICs)
    climates=[]
    while N>0
        p=rand()
        # climate = p<0.1 ? climate_hotdry : ( p<0.2 ? climate_hot : climate_ambient )
        climate = climate_hotdry
        append!(climates,[(climate,false)])
        N-=1
    end
    multiyear(climates,ICs)
end

function ambientyears(N,ICs)
    climates=[]
    while N>0
        p=rand()
        append!(climates,[(climate_ambient,false)])
        N-=1
    end
    multiyear(climates,ICs)
end

function highhailyears(N,ICs)
    climates=[]
    while N>0
        p=rand()
        append!(climates,[(climate_ambient,true)])
        N-=1
    end
    multiyear(climates,ICs)
end

function highhail_hotdryyears(N,ICs)
    climates=[]
    while N>0
        p=rand()
        append!(climates,[(climate_hotdry,true)])
        N-=1
    end
    multiyear(climates,ICs)
end

ICs = Float64[3.3e5,3.3e5,1e6,0.5] # Cn-1 pop, Cn pop, VWn pop, VWn prop infected
N = 10 # how many years to forecast
M = 1 # how many trials to do
println((N,M))

function getmultiyearresults(whichclimate, ICs, N, M)
    Y = Array{Float64,2}(M,N)
    V = Array{Float64,2}(M,N)
    C = Array{Float64,2}(M,N)

    for k in range(1,M)
        results = whichclimate(N,ICs)
        for (j,r) in zip(range(1,N),results)
            C[k,j] = r[1]
            Y[k,j] = r[2]
            V[k,j] = r[3][3]
        end
    end

    if M > 1
        (mean(C,1),std(C,1),mean(Y,1),std(Y,1),mean(V,1),std(V,1)) 
    else
        (C,Y,V)
    end
end

key = ["cheatgrass: ","wheat yield: ","infected proportion wheat: "]

println("ambient years")
R = getmultiyearresults(ambientyears, ICs, N, M)

for (k,l) in zip(key,R)
    println(k,l)
end

println("hot dry years")
R = getmultiyearresults(hotdryyears, ICs, N, M)

for (k,l) in zip(key,R)
    println(k,l)
end

println("high hail years")
R = getmultiyearresults(highhailyears, ICs, N, M)

for (k,l) in zip(key,R)
    println(k,l)
end

println("high hail with hot dry years")
R = getmultiyearresults(highhail_hotdryyears, ICs, N, M)

for (k,l) in zip(key,R)
    println(k,l)
end

# yearly_climates = [(climate_ambient,false), (climate_hot,true), (climate_hotdry,true), (climate_hotdry,false)]
# years = ["climate_ambient_nohail", "climate_hot_hail", "climate_hotdry_hail", "climate_hotdry_nohail"]
# M = multiyear(yearly_climates,ICs)
# c =0
# println("cheatgrass pop, prop yield, prop infected: [old cheatgrass, old vol wheat, wheat, new vol wheat]")
# for m in M
#     c+=1
#     y = years[c]
#     println("Year $c ($y): $m")
# end

