function forwardMap(A::Array{Float64,2},icv::Array{Float64,1},icp::Array{Int,2},rows::Array{Int,1},pow::Int)
    # perform forward mapping on the submatrix of indices in rows
    rows = sort(rows)
    l = length(rows)
    ic = [ icv[k] for k in rows ]
    B = reshape([ A[k,j] for k in rows for j in rows ],l,l)'
    B .*= (ones(l) - ic)
    scaling_factor = sum([ icp[k] for k in rows ])
    ( (eye(l)+B/scaling_factor)^pow ) * ic
end

function test()
    # infection probability: C->C, W->C, C->W, W->W, VW->VW
    # we may need more betas
    const beta = Float64[
                         0.1 0.4 0.4 0.0; 
                         0.5 0.2 0.2 0.2;
                         0.3 0.2 0.05 0.05;
                         0.0 0.2 0.05 0.05;    
                         ]
    const C = 100
    const W = 200
    const VW = 10
    const VWn = 15
    IC_P = [C W VW VWn]
    A = beta.*IC_P
    IC_V = [0, 0, 0.15, 0]
    rows = [1,3,4]
    println("Power of 1")
    println(forwardMap(A,IC_V,IC_P,rows,1)) 
    println("Power of 2 in 1 step")
    println(forwardMap(A,IC_V,IC_P,rows,2))
    V1 = forwardMap(A,IC_V,IC_P,rows,1)
    for (k,r) in enumerate(rows)
        IC_V[r] = V1[k]
    end
    println("Power of 2 in 2 steps")
    println(forwardMap(A,IC_V,IC_P,rows,1))
end

test()