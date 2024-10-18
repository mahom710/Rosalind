def FindMotif(s1,s2):
    # get length of s2, as s2 will always be smaller than s1
    len_s2 = len(s2)

    # initiate final list
    motif_indices = []

    # Iterate through each index of the s1
    for i in range(len(s1)):

        # If the current index of s1's bp starts w/ the same bp as the s2
        if s1[i] == s2[0]:
            # grab a potential motif
            possible_motif = s1[i:i+len_s2]
            # check if it is the same as s2
            if possible_motif == s2:
                motif_indices.append(i+1) # the answer is indexed at 1, python is 0

    return motif_indices

with open("rosalind_gc.txt") as file:
    s1s2 = file.read().split('\n')
    s1 = s1s2[0]
    s2 = s1s2[1]


[print(index) for index in FindMotif(s1,s2)]
