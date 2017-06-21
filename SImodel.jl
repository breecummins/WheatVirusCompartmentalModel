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
    gamma2::Proportion
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

# # The functions forwardMap and stepwise show too much numerical error
# function forwardMap(param::Parameter,icv::Array{Float64,1},rows::Array{Int,1},pow::Int)
#     A = SquareMatrix((param.beta.matrix) .* (param.population'))
#     # perform forward mapping of initial conditions icv on populations pop restricted to indices in rows
#     B = A.matrix .* (1 - icv) / sum(param.population[rows])
#     # zero out entries that are not in rows
#     rem = filter(x -> !(x in rows), 1:A.dim) 
#     B[:,rem] = B[rem,:] = 0
#     # perform the forward map over pow time units
#     ( (eye(A.dim)+B)^pow ) * icv
# end

# function stepwise(param::Parameter,icv::Array{Float64,1},rows::Array{Int,1},pow::Int)
#     # limits numerical error
#     while pow >0
#         icv = forwardMap(param,icv,rows,1)
#         pow -= 1
#     end
#     icv
# end

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

function fullyear(param::Parameter,IC_virus::Array{Float64,1},steps_per_time::Int)
    # volunteer wheat only
    x0 = param.climate.time_periods[1]
    V0 = Float64[0, 1 - ( 1 - IC_virus[2] )*exp(-param.beta.matrix[2,2] * x0), 0, 0]
    # construct transmission/population matrix A
    A = SquareMatrix((param.beta.matrix) .* (param.population'))
    # # alternative method
    # rows0 = [2]
    # V0 = forwardEuler(A,param,IC_virus,rows0,x0,convert(Int,x0*steps_per_time))
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

function multiyear(yearly_climates=Function[], ICs=Float64[]; steps_per_time=500)
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
    results
end

function wheat_yield(param::Parameter,V1::Array{Float64,1},V3::Array{Float64,1},V5::Array{Float64,1})
    Cnplus1 = convert(Int,round(param.tau3.prop*( param.climate.tau1*param.population[1] + param.tau2*param.Cnminus1 ))) 
    Ynplus1 = param.climate.gamma2.prop*( param.gamma11.prop*V1[3] + param.gamma13.prop*(V3[3] - V1[3]) + 1 - V3[3] ) 
    (Cnplus1,Ynplus1)
end

function setparams(climate::Function,ICs::Array{Int,1})
    # ICs=Int[Cnminus1,Cn,VWpop]
    W = convert(Int,2.25e6) # 225 plants/m^2 in one hectare field
    Cnminus1 = ICs[1]
    climate_parameter = climate()
    pop = Int[ICs[2], ICs[3], W, climate_parameter.VWpop]
    beta1=Proportion(0.05)
    beta2=Proportion(0.25)
    beta3=Proportion(0.3)
    beta4=Proportion(0.5)
    beta5= climate_parameter.beta5
    beta = SquareMatrix(Float64[
                         beta1.prop beta2.prop beta2.prop 0.0; 
                         beta3.prop beta5.prop beta4.prop 0.0;
                         beta3.prop beta4.prop beta4.prop 0.0;
                         0.0        0.0        beta4.prop 0.0;    
                         ])
    tau2 = 3.0 # can exceed 1 (cheatgrass plants per plant from previous year)
    tau3 = Proportion(0.1)  # free parameter (competition effect on cheatgrass from wheat)
    gamma11 = Proportion(0.7) # wheat yield given fall infection
    gamma13 = Proportion(0.85) # wheat yield given spring infection
    Parameter(pop,beta,climate_parameter,Cnminus1,tau2,tau3,gamma11,gamma13)
end

function climate_ambient_nohail()
    (VWpop,beta5) = nohail() 
    x0 = 3 # 3 time units = 6 weeks; these should change for hot and hot and dry climate scenarios, but I don't know how yet
    x1 = 2.5 
    x3 = 6
    x4 = 3 
    x5 = 1 
    time_periods = Float64[x0,x1,x3,x4,x5]
    tau1 = 6.0 #free parameter -- should be higher under hot conditions and higher yet under hot and dry conditions
    gamma2 = Proportion(1) #free parameter -- should go down as climate gets worse, should be a function of cheatgrass
    ClimateParameter(VWpop, time_periods, beta5, tau1, gamma2)
end

function climate_ambient_hail()
    (VWpop,beta5) = hail() 
    x0 = 3 # 3 time units = 6 weeks; these should change for hot and hot and dry climate scenarios, but I don't know how yet
    x1 = 2.5 
    x3 = 6
    x4 = 3 
    x5 = 1 
    time_periods = Float64[x0,x1,x3,x4,x5]
    tau1 = 6.0 #free parameter -- should be higher under hot conditions and higher yet under hot and dry conditions
    gamma2 = Proportion(1) #free parameter -- should go down as climate gets worse, should be a function of cheatgrass
    ClimateParameter(VWpop, time_periods, beta5, tau1, gamma2)
end

function climate_hot_nohail()
    (VWpop,beta5) = nohail() 
    x0 = 3 # 3 time units = 6 weeks; these should change for hot and hot and dry climate scenarios, but I don't know how yet
    x1 = 2.5 
    x3 = 6
    x4 = 3 
    x5 = 1 
    time_periods = Float64[x0,x1,x3,x4,x5]
    tau1 = 12.0 #free parameter -- should be higher yet under hot and dry conditions
    gamma2 = Proportion(0.83) #free parameter -- should go down as climate gets worse, should be a function of cheatgrass
    ClimateParameter(VWpop, time_periods, beta5, tau1, gamma2)
end

function climate_hot_hail()
    (VWpop,beta5) = hail() 
    x0 = 3 # 3 time units = 6 weeks; these should change for hot and hot and dry climate scenarios, but I don't know how yet
    x1 = 2.5 
    x3 = 6
    x4 = 3 
    x5 = 1 
    time_periods = Float64[x0,x1,x3,x4,x5]
    tau1 = 12.0 #free parameter -- should be higher yet under hot and dry conditions
    gamma2 = Proportion(0.83) #free parameter -- should go down as climate gets worse, should be a function of cheatgrass
    ClimateParameter(VWpop, time_periods, beta5, tau1, gamma2)
end

function climate_hotdry_nohail()
    (VWpop,beta5) = nohail() 
    x0 = 3 # 3 time units = 6 weeks; these should change for hot and hot and dry climate scenarios, but I don't know how yet
    x1 = 2.5 
    x3 = 6
    x4 = 3 
    x5 = 1 
    time_periods = Float64[x0,x1,x3,x4,x5]
    tau1 = 24.0 #free parameter -- should be higher than the other conditions
    gamma2 = Proportion(0.69) #free parameter -- should go down as climate gets worse, should be a function of cheatgrass
    ClimateParameter(VWpop, time_periods, beta5, tau1, gamma2)
end

function climate_hotdry_hail()
    (VWpop,beta5) = hail() 
    x0 = 3 # 3 time units = 6 weeks; these should change for hot and hot and dry climate scenarios, but I don't know how yet
    x1 = 2.5 
    x3 = 6
    x4 = 3 
    x5 = 1 
    time_periods = Float64[x0,x1,x3,x4,x5]
    tau1 = 24.0 #free parameter -- should be higher than the other conditions
    gamma2 = Proportion(0.69) #free parameter -- should go down as climate gets worse, should be a function of cheatgrass
    ClimateParameter(VWpop, time_periods, beta5, tau1, gamma2)
end

function hail()
    # 100 plants/m^2 in one hectare field
    (convert(Int,1e6),Proportion(0.25))
end

function nohail()
    # 10 plants/m^2 in one hectare field
    (convert(Int,1e5),Proportion(0.025))
end
# # numerical stability testing
# M1 = multiyear([climate_ambient_nohail,climate_ambient_nohail],steps_per_time=20)
# M2 = multiyear([climate_ambient_nohail,climate_ambient_nohail],steps_per_time=100)
# M3 = multiyear([climate_ambient_nohail,climate_ambient_nohail],steps_per_time=500)

# c=0
# for m in zip(M1,M2,M3)
#     c += 1
#     println("Year $c")
#     for n in m
#         println(n)
#     end
# end

yearly_climates = [climate_ambient_nohail,climate_hot_hail,climate_hotdry_hail,climate_hotdry_nohail]
ICs = Float64[3.3e5,3.3e5,1e6,0.5] # Cn-1 pop, Cn pop, VWn pop, VWn prop infected

M = multiyear(yearly_climates,ICs)
c =0
for m in M
    c+=1
    println("Year $c: $m")
end

