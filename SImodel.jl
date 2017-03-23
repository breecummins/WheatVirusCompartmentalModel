immutable SquareMatrix
    matrix::Array{Float64,2}
    dim::Int
    SquareMatrix(matrix,dim) = size(matrix)[1] != size(matrix)[2] ? error("non-square matrix") : new(matrix,size(matrix)[1])
end
SquareMatrix(X) = SquareMatrix(X,size(X)[1])

function forwardMap(A::SquareMatrix,icv::Array{Float64,1},pop::Array{Int,1},rows::Array{Int,1},pow::Int)
    # perform forward mapping of initial conditions icv on populations pop restricted to indices in rows
    B = A.matrix .* (1 - icv) / sum(pop[rows])
    # zero out entries that are not in rows
    rem = filter(x -> !(x in rows), 1:A.dim) 
    B[:,rem] = B[rem,:] = 0
    # perform the forward map over pow time units
    ( (eye(A.dim)+B)^pow ) * icv
end

function test()
    const C = 100
    const W = 200
    const VW = 10
    const VWn = 15
    population = [C, W, VW, VWn]
    # infection probability: C, W, VW, VWn
    # i.e. position beta[1,1] is C -> C probability, beta[2,1] is C -> W, beta[1,2] is W -> C, etc.
    const beta = Float64[
                         0.1 0.4 0.4 0.0; 
                         0.5 0.2 0.2 0.2;
                         0.3 0.2 0.05 0.05;
                         0.0 0.2 0.05 0.05;    
                         ]
    A = SquareMatrix(beta.*(population'))
    IC_virus = Float64[0, 0.1, 0.15, 0]
    rows = Int[1,3,4]
    println("Power of 1")
    println(forwardMap(A,IC_virus,population,rows,1))
    println("Power of 2 in 1 step")
    println(forwardMap(A,IC_virus,population,rows,2))
    println("Power of 2 in 2 steps")
    V1 = forwardMap(A,IC_virus,population,rows,1)
    println(forwardMap(A,V1,population,rows,1))
end

test()