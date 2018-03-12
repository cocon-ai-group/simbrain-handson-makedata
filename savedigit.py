from sklearn import datasets
from PIL import Image

dig = datasets.load_digits()

file1 = open("digits.csv","w")
file2 = open("digits-class.csv","w")

#for i in dig.data:
for j in range(100):
	i = dig.data[j]
	file1.write(','.join(list(map(str,i/16)))+'\n')

#for i in dig.target:
for j in range(100):
	i = dig.target[j]
	d = ['0']*10
	d[i] = '1'
	file2.write(','.join(d)+'\n')

file1.close()
file2.close()

