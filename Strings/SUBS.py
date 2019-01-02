#Given: Two DNA strings s and t (each of length at most 1 kbp).
#Return: All locations of t as a substring of s.

f = open('files/SUBS.txt', 'r')

dna1 = f.readline().strip('\n')
dna2 = f.readline().strip('\n')

positions = []

for i in range(len(dna1)):
    tmp = dna1[i:i+len(dna2)]
    length = len(dna2)
    if dna1[i:i+len(dna2)] == dna2:
       positions.append(i)
       

[print(i+1, end=' ') for i in positions]
    
f.close()