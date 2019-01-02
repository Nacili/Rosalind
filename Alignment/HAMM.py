str1 = 'GTAGAAGTAAGTTGGGAGTGGCGCATGAGGAGCTTTTTTAGACACGACCTCCATAGTCTTAAATCTGATGTAGGACCAGGATACCTAGACTAGCCTAAGTAATCGTCACAGGGGTAATGCTCCCACTTAGTTCCCGATGATCGCAGTCGCCTATGGCACGAGCAGGCTATTGGCCTGTATAAGAATGTTCCGCGGCAAAGTCCACGCGGAGAAGCACTCCGCGTCCGAAAGCATCCGCTACATAGTGAAGTTCCCAAAACGGCTGCACCGTTTTATACTGTCATAATTATCTCACTTTATGCTATGGTAATTGATACAGCAGCACGGGGGGGTGTCAGGTCGACTATGATCTAGCCCTTCCTCTAGGGCCTGGGTCATATTGACTTTTTTAGCGGATAGCATTACCTGACTGAAAGTCATGTTAGCACCATAGCAACCTTTGACGGTCCAACGTAGGTATTCCCTTGGCCTACGCGGGGTGATCGGTGACCACCATCATGCACTTTGCCTCATAGATTCCCCCAATGCGTGGAGTCTAGAGCCACGGCCTCGGACTGGTAACTCTCATTTTTCAGACCCCGTTTATGGGTTCTATAGTTGCGTCTATCTTGCCTTTTCCCCTGCTAATTTGTGCTAGTGATATACAGCGGAAAGAGTGACGCCCTTATCCCTGCCAATTGTGGCGAGGCGACCTCCATAGACCATCCGCTCATCCCTAGGACAGAAACCTGTCATCATTTCAAGCGGTAATCCCCGAAGATTACGGTCTTTGTCGGTCTACGGACACTCATTAGCATTGATATTCATGTTTATCTTATAAGTATCATCACCAAAGCTGCGCCAGAAAATGCGCTCAGACATCAGTCGTAAGCACACAGTGTGGGGTTTCCCTACCCTCATAACACGGTCCTGATCGAGGTCATCTAGAGTAGTTAAGGGTCTCAAC'
str2 = 'GTAAAGGAAACATAGCCGCAACCTATCACGATATTTTTTGTTCTTAGAGTCCACACGCTTATATCTGAACGAGCATTAGGACGTGCAGACACAACTAATTTGACGTAAGCGGGGCATTGTAACGCACACGGTCACGAGAGTTGCAGCCTACTAAGGCGCCCCCACGCTGTAAGGCCTTTGACGAAAAAACCGCAATTACGGGTCCCTACAGATAAACTGCGCGTGATACGCACACCCCTAGAGAAAGACGATTCCGAAAGCTCTCCGACGTCTAATCCTGGGGTAGTCACCTCACACTAAACATACTTAATTGACATGGCAGAAGCAGAGGGTGTGCCGATTCGTATGTTCTACAGCAAATTCTAAGCCATAGGTCGTCTCTACTATTTTAGCCATTACGATTAACACGCTGTACGTGGAGTGAGCTCCAATGATACCTATTCTGGGCCAGGGATGTCTTCTCATTCCTATGCGCTTGTTGAACCGTCTCCCAGTTTGTGCACAGCGCCTAGGAGATACCACCCGGCGGCTATAAACAGGTCCACGGTGTCAGGCTTGTAAGTCGAACTTTCTAGACCTCGCGGTGGGATTGGAGACCATCGGCTATTCGGGGCATTACGCGGCCATTTGCAAGCCGTATTCTGCGCATTAAAGAACGACGCTGTTATTAGAGCCATGAAGGCGAAGGTCGCCCACAAAGACAATGCACCCCGCCCCCGAACGCAAACCTGATAACTATGCAAGCCCTTAAGGCCGACAATAACTGTCTTGGTCGATGTACGGTCGCTAGTTAGTAGCCCATGTCAAGAGAAGATCAGACATATAATTATCGCATGTGTACAAAAATTTTCACTAAGTCTAAATTAGATCGCATATTAGGATGTTAATGGTGTAGGTATTAAGACAATCCCCGTCCAAGTTGGGCATAGTAGTTTATCCGCTCAGC'

#hamm distance
#dh = 0
#
#for i in range(len(str1)):
#    if str1[i] != str2[i]:
#        dh = dh+1
#        
#print(dh)

#better way
print(sum(a != b for a, b in zip(str1, str2)))