def HammingDistance(s1,s2):

    # Intialize the count
    count = 0

    # Check if each residue is the same
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            count += 1

    return count

with open('rosalind_gc.txt','r') as file:
    temp = file.read().split('\n')
    s1 = temp[0]
    s2 = temp[1]

print(HammingDistance(s1,s2))