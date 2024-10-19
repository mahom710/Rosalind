from math import factorial


def HeteroChildren(n,k):

    # Create binomial function
    def Binomial(num_child,num_suc,prob_suc):
        coef = factorial(num_child)/(factorial(num_suc)*factorial(num_child-num_suc))
        final_prob = coef * (prob_suc**num_suc) * (1-prob_suc)**(num_child-num_suc)
        return final_prob

    # how many children are in the kth gen
    num_children = 2**k

    # list of at least n children being hetero
    num_hetero_child_list = list(range(n,num_children+1))
    print(num_hetero_child_list)

    # loop through function
    final_prob = sum([Binomial(num_children, child_group, 0.25) for child_group in num_hetero_child_list])

    return final_prob

print(HeteroChildren(8,5))



