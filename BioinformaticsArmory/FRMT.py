from Bio import Entrez
from Bio import SeqIO

Entrez.email = 'nadezdabogdanovic1@gmail.com'
handle = Entrez.efetch(db="nucleotide", id=["NM_001194889, NM_001271262, JX308813, BT149870, JX205496, NM_204821, JQ867082, JX280897"], rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))

length = float('inf')
j = 0
for i in records:
    if len(i.seq) < length:
        length = len(i.seq)
        j = i

print(">" + j.description)
print(j.seq)


print(records)