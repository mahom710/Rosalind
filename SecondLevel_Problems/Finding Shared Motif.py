def ReadFastq(file_path):
    # create empty vars
    id_list = []
    seq_list = []

    # read in file
    with open(file_path, 'r') as file:
    # create empty seq to start
        seq = ''
        for line in file:
            line = line.strip()
            if line[0] == '>':
                id_list.append(line[1:])
                # account for the first id
                if seq:
                    seq_list.append(seq)
                    seq = ''  # reset the seq
            else:
                seq = seq + line
        # account for the last sequence
        seq_list.append(seq)

    return id_list, seq_list



def SharedMotif(seq_list):
    # find the shortest sequence
    min_len = 999999999 # random really large number
    for seq in seq_list:
        cur_len = len(seq)
        if cur_len < min_len:
            min_len = cur_len
            min_seq = seq

    # create every possible motif from it
    motifs = []

    for i in range(min_len):
        # the start of a possible motif
        motif = min_seq[i]
        for j in range(i+1,min_len):
        # add the next bp to the start of each motif, append it to the list, and continue to the end
            motif = motif + min_seq[j]
            motifs.append(motif)

    # order the motifs
    motifs.sort(key=len)
    motifs_ordered = []
    for m in motifs:
        motifs_ordered = [m] + motifs_ordered

    # Search every sequence in order of decreaseing size motifs
    for motif in motifs_ordered:
        # start truth list
        motif_in_all = []
        # check if every sequence has the motif
        for seq in seq_list:
            if motif in seq:
                motif_in_all.append(True)
            else:
                motif_in_all.append(False)
        # if every value is True, then that is the motif and break the loop
        if len(set(motif_in_all)) == 1:
            final_motif = motif
            break

    print(final_motif)

    # another idea is using some form of intersect



# call everything
id_list, seq_list = ReadFastq('rosalind_test.txt')
SharedMotif(seq_list)


