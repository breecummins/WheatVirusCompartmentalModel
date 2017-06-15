type SquareMatrix
    matrix::Array{Float64,2}
    dim::Int
    SquareMatrix(matrix,dim) = size(matrix)[1] != size(matrix)[2] ? error("non-square matrix") : new(matrix,size(matrix)[1])
end
SquareMatrix(X) = SquareMatrix(X,size(X)[1])

type Proportion
    prop::Float64
    Proportion(prop) = !(0 < prop <1) ? error("not a proportion") : new(prop)
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

function fullyear(param::Parameter,IC_virus = Float64[0, 0.5, 0, 0])
    # volunteer wheat only
    rows0 = [2]
    x0 = param.time_periods[1]
    V0 = stepwise(param,IC_virus,rows0,x0)
    param.beta.matrix[2,2] = 0.0 # volunteer wheat no longer directly transmits to itself
    # volunteer wheat -> wheat and cheatgrass
    # this is split into 3 different steps to record differing yield loss to infection
    rows1 = [1,2,3]
    x1 = param.time_periods[2]
    V1 = stepwise(param,V0,rows1,x1)
    # growth period after hibernation
    x3 = param.time_periods[3]
    V3 = stepwise(param,V1,rows1,x3)
    # plant growth ends
    x4 = param.time_periods[4]
    V4 = stepwise(param,V3,rows1,x4)
    # wheat -> new volunteer wheat
    rows5 = [3,4]
    x5 = param.time_periods[5]
    V5 = forwardMap(param,V4,rows5,x5)
    (V1,V3,V5)
end

function multiyear(num_years::Int,param::Parameter,IC_virus = Float64[0, 0.5, 0, 0])
    results = []
    while num_years > 0
        (V1,V3,V5) = fullyear(param,IC_virus)
        (Cnplus1,VWnplus1,Ynplus1) = stats(param,V1,V3,V5)
        append!(results,[(Cnplus1,VWnplus1,Ynplus1)])
        IC_virus = Float64[0, VWnplus1, 0, 0]
        param.population[1] = Cnplus1
        num_years -= 1
    end
    results
end

function stats(param::Parameter,V1::Array{Float64,1},V3::Array{Float64,1},V5::Array{Float64,1})
    println(V5[3]) # percentage infected wheat
    Cnminus1 = 0.9*param.population[1] #fake initial condition -- need this value from 2 years back
    VWnplus1 = V5[4]
    Cnplus1 = convert(Int,round(0.8*( 1.1*param.population[1] + 0.2*Cnminus1 ))) # 3 fake params
    Ynplus1 = 0.85*( 0.25*V1[3] + 0.5*(V3[3] - V1[3]) + 1 - V3[3] ) # 3 fake params
    (Cnplus1,VWnplus1,Ynplus1)
end

function setparams(climate,ICs=Int[Cnminus1,Cn,VWpop])
    C = 1000
    VWpop = 100
    W = convert(Int,2e7)
    VWnpop = 150
    pop = Int[C, VWpop, W, VWnpop]
    beta = SquareMatrix(Float64[
                         0.1 0.8 0.8 0.0; 
                         0.5 0.1 0.6 0.0;
                         0.5 0.6 0.6 0.0;
                         0.0 0.0 0.6 0.0;    
                         ])
    Parameter(pop,beta,time_periods)
end

function climate_ambient(W)
    VWpop = convert(Int,round(0.05*W))
    x0 = 2 # 2 time units = 4 weeks
    x1 = 3 
    x3 = 4 
    x4 = 2 
    x5 = 1 
    time_periods = Int[x0,x1,x3,x4,x5]
    tau1 = 1.1
    gamma2 = 0.96 #will be multiplied by C
    (VWpop, time_periods, tau1, gamma2)
end




param = setparams()
println(stats(param,fullyear(param)...))
println(multiyear(2,param))
