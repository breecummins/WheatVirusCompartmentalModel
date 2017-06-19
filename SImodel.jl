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
    time_periods::Array{Int}
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

function getA(p::Parameter)
   SquareMatrix((p.beta.matrix) .* (p.population')) 
end

function forwardMap(param::Parameter,icv::Array{Float64,1},rows::Array{Int,1},pow::Int)
    A = getA(param)
    # perform forward mapping of initial conditions icv on populations pop restricted to indices in rows
    B = A.matrix .* (1 - icv) / sum(param.population[rows])
    # zero out entries that are not in rows
    rem = filter(x -> !(x in rows), 1:A.dim) 
    B[:,rem] = B[rem,:] = 0
    # perform the forward map over pow time units
    ( (eye(A.dim)+B)^pow ) * icv
end

function stepwise(param::Parameter,icv::Array{Float64,1},rows::Array{Int,1},pow::Int)
    # limits numerical error
    while pow >0
        icv = forwardMap(param,icv,rows,1)
        pow -= 1
    end
    icv
end

function tinysteps(param::Parameter,icv::Array{Float64,1},rows::Array{Int,1},pow::Int,numsteps::Int = 20*pow)
    # limits numerical error
    timestep = pow/numsteps
    A = getA(param)
    while numsteps >0
        # perform forward mapping of initial conditions icv on populations pop restricted to indices in rows
        B = A.matrix .* (1 - icv) / sum(param.population[rows])
        # zero out entries that are not in rows
        rem = filter(x -> !(x in rows), 1:A.dim) 
        B[:,rem] = B[rem,:] = 0
        icv = (eye(A.dim) + timestep*B)*icv
        numsteps -= 1
    end
    icv
end

function fullyear(param::Parameter,IC_virus = Float64[0, 0.5, 0, 0])
    # volunteer wheat only
    rows0 = [2]
    x0 = param.climate.time_periods[1]
    V0 = tinysteps(param,IC_virus,rows0,x0)
    param.beta.matrix[2,2] = 0.0 # volunteer wheat no longer directly transmits to itself
    # volunteer wheat -> wheat and cheatgrass
    # this is split into 3 different steps to record differing yield loss to infection
    rows1 = [1,2,3]
    x1 = param.climate.time_periods[2]
    V1 = tinysteps(param,V0,rows1,x1)
    # growth period after hibernation
    x3 = param.climate.time_periods[3]
    V3 = tinysteps(param,V1,rows1,x3)
    # plant growth ends
    x4 = param.climate.time_periods[4]
    V4 = tinysteps(param,V3,rows1,x4)
    # wheat -> new volunteer wheat
    rows5 = [3,4]
    x5 = param.climate.time_periods[5]
    V5 = tinysteps(param,V4,rows5,x5)
    (V1,V3,V5)
end

function multiyear(num_years::Int,param::Parameter,IC_virus = Float64[0, 0.5, 0, 0])
    results = []
    while num_years > 0
        println(IC_virus)
        (V1,V3,V5) = fullyear(param,IC_virus)
        println((V1,V3,V5))
        (Cnplus1,Ynplus1) = stats(param,V1,V3,V5)
        append!(results,[(Cnplus1,param.climate.VWpop,Ynplus1)])
        IC_virus = Float64[0, V5[4], 0, 0]
        param.Cnminus1 = param.population[1]
        param.population[1] = Cnplus1
        param.population[2] = param.climate.VWpop
        num_years -= 1
    end
    results
end

function stats(param::Parameter,V1::Array{Float64,1},V3::Array{Float64,1},V5::Array{Float64,1})
    VWnplus1 = param.climate.VWpop # constant for now -- will need to add climate functions later
    Cnplus1 = convert(Int,round(param.tau3.prop*( param.climate.tau1*param.population[1] + param.tau2*param.Cnminus1 ))) 
    Ynplus1 = param.climate.gamma2.prop*( param.gamma11.prop*V1[3] + param.gamma13.prop*(V3[3] - V1[3]) + 1 - V3[3] ) 
    (Cnplus1,Ynplus1)
end

function setparams(climate::Function,ICs::Array{Int,1})
    # ICs=Int[Cnminus1,Cn,VWpop]
    W = convert(Int,2e7) # plants in one hectare field
    Cnminus1 = ICs[1]
    climate_parameter = climate(W)
    pop = Int[ICs[2], ICs[3], W, climate_parameter.VWpop]
    beta = SquareMatrix(Float64[
                         0.1 0.8 0.8 0.0; 
                         0.5 0.1 0.6 0.0;
                         0.5 0.6 0.6 0.0;
                         0.0 0.0 0.6 0.0;    
                         ])
    tau2 = 0.4 #can exceed 1
    tau3 = Proportion(0.9)
    gamma11 = Proportion(0.25)
    gamma13 = Proportion(0.5)
    Parameter(pop,beta,climate_parameter,Cnminus1,tau2,tau3,gamma11,gamma13)
end

function climate_ambient_nohail(W)
    VWpop = convert(Int,round(0.05*W))
    x0 = 2 # 2 time units = 4 weeks
    x1 = 3 
    x3 = 4 
    x4 = 2 
    x5 = 1 
    time_periods = Int[x0,x1,x3,x4,x5]
    tau1 = 1.1
    gamma2 = Proportion(0.96)
    ClimateParameter(VWpop, time_periods, tau1, gamma2)
end

function climate_ambient_hail(W)
    VWpop = convert(Int,round(0.2*W))
    x0 = 2 # 2 time units = 4 weeks
    x1 = 3 
    x3 = 4 
    x4 = 2 
    x5 = 1 
    time_periods = Int[x0,x1,x3,x4,x5]
    tau1 = 1.1
    gamma2 = Proportion(0.96)
    ClimateParameter(VWpop, time_periods, tau1, gamma2)
end



param = setparams(climate_ambient_nohail,Int[convert(Int,1e6),convert(Int,2.5e6),convert(Int,1e5)])
println(stats(param,fullyear(param)...))
println(multiyear(2,param))
