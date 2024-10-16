def ReverseComplement(seq):
    #intiate the rc list
    rc = ""

    for bp in seq:
        # get comp
        if bp == 'A':
            bp = 'T'
        elif bp == 'T':
            bp = 'A'
        elif bp == 'C':
            bp = 'G'
        elif bp == 'G':
            bp = 'C'

        # reverse
        rc = bp + rc

    return rc