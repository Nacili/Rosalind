f = open('files/GC.fasta', 'r')

lines = f.readlines()
resultLine = 0
numLines = -1
resultSum = 0
headingLines = []
sequence = ''

for i in range(len(lines)):
    if lines[i][0] == '>':
        headingLines.append(lines[i].strip('\n'))
        numLines = numLines + 1
        if i != 0:
            g = sequence.count('G')
            c = sequence.count('C')
            s = len(sequence)
            tmp = (g+c)/s*100
            if tmp > resultSum:
                resultSum = tmp
                resultLine = numLines - 1
        sequence = ''
    else:
        sequence = sequence + lines[i].strip('\n')
        
g = sequence.count('G')
c = sequence.count('C')
s = len(sequence)   
tmp = (g+c)/s*100 
if tmp > resultSum:
    resultSum = tmp
    resultLine = numLines
    
print(headingLines[resultLine][1:])
print(resultSum)


f.close()