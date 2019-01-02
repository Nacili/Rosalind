k = 25 #homo-dominants
m = 25 #hetero
n = 16 #homo-recesives

alls = k+m+n

# probability that X is DD and Y can be anny and child has dominant phenotype
p_X_DD = k/alls
p_X_DD_Y_DD_dominant = p_X_DD * ((k-1)/(alls-1))
p_X_DD_Y_Dd_dominant = p_X_DD * (m/(alls-1))
p_X_DD_Y_dd_dominant = p_X_DD * (n/(alls-1))

# probability that X is Dd and Y can be anny and child has dominant phenotype
p_X_Dd = m/alls
p_X_Dd_Y_DD_dominant = p_X_Dd*(k/(alls-1))
p_X_Dd_Y_Dd_dominant = p_X_Dd*((m-1)/(alls-1))*3/4
p_X_Dd_Y_dd_dominant = p_X_Dd*(n/(alls-1))*1/2

# probability that X is dd and Y can be anny and child has dominant phenotype
p_X_dd = n/alls
p_X_dd_Y_DD_dominant = p_X_dd*(k/(alls-1))
p_X_dd_Y_Dd_dominant = p_X_dd*(m/(alls-1))*1/2
#p_X_dd_Y_dd_dominant = p_X_dd*((n-1)/(alls-1))*0

result = p_X_DD_Y_DD_dominant + p_X_DD_Y_Dd_dominant + p_X_DD_Y_dd_dominant + p_X_Dd_Y_DD_dominant + p_X_Dd_Y_Dd_dominant + p_X_Dd_Y_dd_dominant + p_X_dd_Y_DD_dominant + p_X_dd_Y_Dd_dominant

print(result)