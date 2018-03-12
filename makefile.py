# -*- coding: utf-8 -*-
import numpy as np

num_val = 50

r = 2 * np.random.random_sample(size=(num_val,2)) - 1 # -1から1までの範囲

file1 = open("data.csv","w")
file2 = open("class1.csv","w")
file3 = open("class2.csv","w")

for i in range(num_val):
	if r[i][0] > r[i][1]:
		clz1 = 0
	else:
		clz1 = 1

	if r[i][0] > 0 and r[i][1] > 0:
		clz2 = 0 if r[i][0] > r[i][1] else 1
	elif r[i][0] > 0 and r[i][1] <= 0:
		clz2 = 0 if r[i][0] > -r[i][1] else 1
	elif r[i][0] <= 0 and r[i][1] > 0:
		clz2 = 0 if -r[i][0] > r[i][1] else 1
	else:
		clz2 = 0 if -r[i][0] > -r[i][1] else 1

	file1.write("%f,%f\n"%(r[i][0],r[i][1]))
	file2.write("%d,%d\n"%(clz1,1-clz1))
	file3.write("%d,%d\n"%(clz2,1-clz2))

file1.close()
file2.close()
file3.close()


