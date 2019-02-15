from statistics import mean


collumn=[[10, 20], [30, 40, 50, 60, 70]]
collumnData=collumn[1][1:]
#collumnData=niceData[colCounter][1:]   #The rest of the elements in each collumn are data points.
collumnMean= mean(collumnData)
#collumnStdev= stdev(collumnData)
#collumnVar=variance(collumnData)
#collumnMin=min(collumnData)
#collumnMax=max(collumnData)
print(collumnMean)
