import itertools
import math

def GeneOrders(n):

    with open('answer.txt','w') as file:

        # get the number of possible permutations
        num_permutations = math.factorial(n)

        # print out each permutation
        all_perms = itertools.permutations(list(range(1,n+1)),n)
        file.write(f'{num_permutations}\n')

        for perm in all_perms:
            string = ''
            for p in perm:
                string = string + ' ' + str(p)
            string = string.strip()
            file.write(f'{string}\n')

GeneOrders(6)