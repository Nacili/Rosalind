from Bio import Entrez

Entrez.email = ''
handle = Entrez.esearch(db='nucleotide', term='("Pyrus"[Organism]) AND ("2005/11/27"[PDAT] : "2006/06/07"[PDAT])')
record = Entrez.read(handle)
print(record['Count'])