def EvOffspring(n1,n2,n3,n4,n5,n6):
    # probabilities of each allele pair having dominant child
    p1 = 1
    p2 = 1
    p3 = 1
    p4 = 0.75
    p5 = 0.5
    p6 = 0

    # expected value
    ev = 2*(p1*n1 + p2*n2+ p3*n3+ p4*n4+ p5*n5+ p6*n6) # x2 bc every pair has 2 children

    return ev

print(EvOffspring(17892, 17469, 18580, 16808, 16833, 16120))