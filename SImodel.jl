# infection probability: C->C, W->C, C->W, W->W, VW->VW
# we may need more betas -- could be that just the beta' are equal
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

function forwardMap(rows::Array{Int},ic::Array{Float64,1},pow::Int)
    l = length(rows)
    B = [ A[k,j] for k in rows for j in rows ]
    B = reshape(B,l,l)
    B = B.*(ones(l) - ic)
    ( (eye(l)+B)^pow ) * ic
end

println(forwardMap([1 2 3 4],IC_V,1))