import numpy

f = open('files/CONS.fasta', 'r')
lines = f.readlines()

j = 0
i = 0
while i < len(lines):
    line = lines[i]
    if lines[i][0] == '>':
        j = i
        lines.remove(lines[i])
        i = i+1
    else:
        lines[j] = lines[j].strip('\n') + lines[i].strip('\n')
        lines.remove(lines[i])

#i=0
#ind = 0
#while i < len(lines):
#    if i%2 == 1:
#        lines[i-1] = lines[i].strip('\n')
#        lines.remove(lines[i])
#        ind = 1
#    else:
#        if ind == 1:
#            lines[i-1] = lines[i].strip('\n')
#            lines.remove(lines[i])
#            ind = 0
#    i = i+1
   
    

#making profile and consensus
profile = numpy.zeros((4, len(lines[0])), dtype=int)
i = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'A':
            profile[0][j] = profile[0][j] + 1
        if lines[i][j] == 'C':
            profile[1][j] = profile[1][j] + 1
        if lines[i][j] == 'G':
            profile[2][j] = profile[2][j] + 1
        if lines[i][j] == 'T':
            profile[3][j] = profile[3][j] + 1
    
#consensus        
maxEl = numpy.argmax(profile, axis=0)

for i in maxEl:
    if i == 0:
        print('A', end='')
    if i == 1:
        print('C', end='')
    if i == 2:
        print('G', end='')
    if i == 3:
        print('T', end='')
        
print()
        

for i in range(len(profile)):
    if i == 0:
        print('A: ', end=' ')
    if i == 1:
        print('C: ', end=' ')
    if i == 2:
        print('G: ', end=' ')
    if i == 3:
        print('T: ', end=' ')
    for j in profile[i]:
        print(j, end=' ')
    print()

f.close()