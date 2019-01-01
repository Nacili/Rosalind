from Bio.Seq import Seq

my_seq = Seq('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
A = my_seq.count('A')
C = my_seq.count('C')
G = my_seq.count('G')
T = my_seq.count('T')

print(str(A) + " " + str(C) + " " + str(G) + " " + str(T))

#other solution without Seq
sequence = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC';
A = sequence.count('A')
C = sequence.count('C')
G = sequence.count('G')
T = sequence.count('T')

print(str(A) + " " + str(C) + " " + str(G) + " " + str(T))