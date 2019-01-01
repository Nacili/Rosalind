#Given: A set of protein strings in FASTA format that share some motif with
#minimum length 20.
#Return: Regular expression for the best-scoring motif.
#Note: MEME Suite (http://meme.nbcr.net/meme/) is required to run this code

f = open('files/meme.txt', 'r')

lines = f.readlines()
line_num = -1
for i in lines:
    line_num = line_num + 1
    if 'regular expression' in i and (abs(i.find('Motif') - i.find('MEME')))>=20:
        print(lines[line_num+2])



f.close()
