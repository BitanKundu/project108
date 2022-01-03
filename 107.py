data1=[20,30,40,50]
data2=[70,80,90,100]
from scipy.stats import pearson
corr,_=pearsonr(data1,data2)
print(corr)

numberofcoffees=[5,2,10,7,3,1]
hoursofsleep=[10,14,3,6,11,16]
corr,_=pearsonr(numberofcoffees,hoursofsleep  )