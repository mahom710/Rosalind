def reversecomp(seq):
    # create reverse comp
    comp_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    rc = [comp_dict[bp] for bp in seq[::-1]]
    return ''.join(rc)

def FindRestrictSites(seq):
    # final list
    final_list = []
    size = ''

    # loop through each
    for i in range(len(seq)):

        # create loop to check window size
        for win in range(4,13):
            # make sure it doesn't go out of bound

            if i+win <= len(seq):
                # create the current seq and rc of that
                cur_seq = seq[i:i+win]
                cur_rc = reversecomp(cur_seq)

                # check current size
                if cur_seq == cur_rc:
                    size = win

            if size:
                final_list.append([i+1,size])
                print(f'{i+1} {size}')
                size = '' # reset the size


    return final_list

with open('rosalind_test.txt') as file:
    seq = ''
    for line in file:
        seq += line.strip()

# Run function
print(seq)
FindRestrictSites(seq)
