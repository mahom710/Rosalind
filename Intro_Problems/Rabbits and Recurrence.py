def Rabbits(n,k):
    # Intial set
    sequence = [1,1]

    # add the last 2 and append to the end
    for i in range(2,n):
        next_num = sequence[i-2]*k + sequence[i-1]
        sequence.append(next_num)
        print(sequence)

    return sequence[-1]