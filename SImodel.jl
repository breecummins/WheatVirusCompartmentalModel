type SquareMatrix
    matrix::Array{Float64,2}
    dim::Int
    SquareMatrix(matrix,dim) = size(matrix)[1] != size(matrix)[2] ? error("non-square matrix") : new(matrix,size(matrix)[1])
end
SquareMatrix(X) = SquareMatrix(X,size(X)[1])

type Parameter
    population::Array{Int}
    beta::SquareMatrix
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


function fullyear(IC_virus = Float64[0, 0.5, 0, 0])
    param = setparams()
    Cnminus1 = 0.9*param.population[1] #fake param
    rows = [2]
    x0 = 2 # 1 time unit = 2 weeks, fake param
    # V0 = forwardMap(param,IC_virus,rows,x0)
    V0 = stepwise(param,IC_virus,rows,x0)
    param.beta.matrix[2,2] = 0.0
    rows = [1,2,3]
    x1 = 3 #fake param
    # V1 = forwardMap(param,V0,rows,x1)
    V1 = stepwise(param,V0,rows,x1)
    x3 = 4 #fake param
    # V3 = forwardMap(param,V1,rows,x3)
    V3 = stepwise(param,V1,rows,x3)
    x4 = 2 #fake param
    # V4 = forwardMap(param,V3,rows,x4)
    V4 = stepwise(param,V3,rows,x4)
    rows = [3,4]
    x5 = 1 #fake param
    V5 = forwardMap(param,V4,rows,x5)
    println(V5[3])
    VWnplus1 = V5[2]
    Cnplus1 = 0.8*( 1.1*param.population[1] + 0.2*Cnminus1 ) # 3 fake params
    Ynplus1 = 0.85*( 0.25*V1[3] + 0.5*(V3[3] - V1[3]) + 1 - V3[3] ) # 3 fake params
    (Cnplus1,VWnplus1,Ynplus1)
end

function setparams()
    C = 100
    VW = 10
    W = 200
    VWn = 15
    pop = [C, VW, W, VWn]
    # beta = SquareMatrix(Float64[
    #                      0.1 0.8 0.8 0.0; 
    #                      0.5 0.1 0.6 0.0;
    #                      0.5 0.6 0.6 0.0;
    #                      0.0 0.0 0.6 0.0;    
    #                      ])
    beta = SquareMatrix(0.001*Float64[
                         0.1 0.8 0.8 0.0; 
                         0.5 0.1 0.6 0.0;
                         0.5 0.6 0.6 0.0;
                         0.0 0.0 0.6 0.0;    
                         ])
    # beta = SquareMatrix(0.9*ones(4,4))
    Parameter(pop,beta)
end



function test()
    C = 100
    W = 200
    VW = 10
    VWn = 15
    population = [C, W, VW, VWn]
    # infection probability: C, W, VW, VWn
    # i.e. position beta[1,1] is C -> C probability, beta[2,1] is C -> W, beta[1,2] is W -> C, etc.
    const beta = SquareMatrix(Float64[
                         0.1 0.4 0.4 0.0; 
                         0.5 0.2 0.2 0.2;
                         0.3 0.2 0.05 0.05;
                         0.0 0.2 0.05 0.05;    
                         ])
    param = Parameter(population,beta)
    # A = SquareMatrix( (beta.matrix) .* (population') )
    IC_virus = Float64[0, 0.1, 0.15, 0]
    rows = Int[1,3,4]
    println("Power of 1")
    println(forwardMap(param,IC_virus,rows,1))
    println("Power of 2 in 1 step")
    println(forwardMap(param,IC_virus,rows,2))
    println("Power of 2 in 2 steps")
    V1 = forwardMap(param,IC_virus,rows,1)
    println(forwardMap(param,V1,rows,1))
end

# test()
println(fullyear())
