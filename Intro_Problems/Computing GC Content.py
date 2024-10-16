# Without the use of packages

file_path = 'Intro_Problems/rosalind_gc.txt'
with open(file_path, 'r') as f:
    fastq = f.read()

# intiate gc
max_gc = 0

# split the fastq
split_fastq = fastq.split('>')[1:]

for read in split_fastq:
    seq = ''.join(read.split('\n')[1:])
    num_c = seq.count('C')
    num_g = seq.count('G')
    gc = num_c + num_g
    percent_gc = gc / len(seq)

    # Find the max
    if percent_gc > max_gc:
        max_gc = percent_gc
        # return the ID
        id = ''.join(read.split('\n')[0])

print(f"{id}\n{max_gc * 100}")
