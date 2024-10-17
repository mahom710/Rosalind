def Mendel(k,m,n):
# This problem is a combinations problem as order of the organisms does not matter and does not get replaced (organisms must mate with another one)
    # figure out the combinations of every pair
    def combinations_of_same_pairs(x):
        # equation to find combinations of
        return x*(x-1)/2

    total = k+m+n
    total_pairs = combinations_of_same_pairs(total)

    # figure out probability of each pair type giving dominant
    prob_kk = combinations_of_same_pairs(k) / total_pairs # just has to be phenotypically dominant, so its just that odds that we get a k and k without order mattering, combos are important bc there is no replacement
    prob_km = k*m / total_pairs # k*m bc this is all the combos of k and m, no need for combination equation
    prob_kn = k*n / total_pairs # same as above
    prob_nm = m*n / total_pairs * 0.5 # there is a 50% chance a hetero and recessive give a phenotypically dominant
    prob_nn = 0 # this will always be 0% to give a dom
    prob_mm = combinations_of_same_pairs(m) / total_pairs * 0.75

    # add all the probabilities up
    total_prob = prob_kk+prob_km+prob_kn+prob_nm+prob_nn+prob_mm # these are all mutually exlucsive, or paths in the prob tree, so we add them up

    return total_prob

