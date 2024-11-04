def ReadFastq(path):
    # read it in
    with open(path,'r') as file:
        # create lsit
        id_list = []
        seq_list = []
        seq = ''

        for line in file:
            # strip the file
            line = line.strip()

            if line[0] == '>':
                id_list.append(line[1:])
                if seq: # account for first read
                    seq_list.append(seq)
                    # reset seq
                    seq = ''
            else:
                seq = seq + line
        # append the final seq
        seq_list.append(seq)
    return id_list, seq_list


def FindSharedMotif(seq_list):
    # find the shortest seq in the list
    smol_seq = sorted(seq_list, key=len)[0]

    # create every possible motif
    all_motifs = []

    for i in range(len(smol_seq)):
        for j in range(i+1,len(smol_seq)):
            all_motifs.append(smol_seq[i:j])

    # sort the motif
    all_motifs.sort(key=len,reverse=True)

    # search every seq for the motif, break the loop when it finds it
    for motif in all_motifs:
        # reset the truth list
        truth_list = []

        for seq in seq_list:
            # check if motif is in every seq
            if seq.find(motif) >= 0:
                truth_list.append(True)
            else:
                truth_list.append(False)

        # check the truth list
        if len(set(truth_list)) == 1:
            final_motif = motif
            break

    return final_motif



# PROGRAM #
id_list, seq_list = ReadFastq('rosalind_test.txt')
print(FindSharedMotif(seq_list))



