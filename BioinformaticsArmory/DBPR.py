#Given: The UniProt ID of a protein.
#Return: A list of biological processes in which the protein is involved
#(biological processes are found in a subsection of the protein's "Gene Ontology"
#(GO) section).

from Bio import ExPASy
from Bio import SwissProt

#reading for given protein ID
handle = ExPASy.get_sprot_raw('Q07281')
#parse
record = SwissProt.read(handle)
#reading lines in gene.txt
result = record.cross_references
#we need information about processes, label P: in file
#lebel F: is function
for i in range(len(result)):
    if result[i][0] == 'GO':
        res = result[i]
        for j in range(len(res)):
            if res[j][0][0] == 'P':
                print(res[j][2:])
                
