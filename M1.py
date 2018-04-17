import pdb
import csv
import sys
from   scipy import ndimage, misc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import itertools

#Run with sys.argv[1] = annotations file, sys.argv[2] = number of partitions, sys.argv[3] = how many range values to find

def file_block(fp, number_of_blocks, block):
	assert 0 <= block and block < number_of_blocks
	assert 0 < number_of_blocks
	fp.seek(0,2)
	file_size = fp.tell()
	ini = file_size * block / number_of_blocks
	end = file_size * (1 + block) / number_of_blocks

	if ini <= 0:
		fp.seek(0)
	else:
		fp.seek(ini-1)
		fp.readline()
	while fp.tell() < end:
		yield fp.readline()

if __name__ == '__main__':
	fp = open(sys.argv[1])
	number_of_chunks = int(sys.argv[2])
	k = int(sys.argv[3])
	for chunk_number in range(number_of_chunks):
		print 100 * '='
		matr = np.zeros((500,500))
		i = 0
		for line in file_block(fp, number_of_chunks, chunk_number):
			currentLine = line.split(",")
			xmin = int(currentLine[0])
			ymax = int(currentLine[1])
			width = int(currentLine[2])
			height = int(currentLine[3])
			xmax = xmin + width;
			ymin = ymax - height;
			matr[(xmin-1):xmax, (ymin-1):ymax] = matr[(xmin-1):xmax, (ymin-1):ymax] + 1
			i = i + 1
		conc = np.divide(matr, i)
		## M1 ##
		flat = conc.flatten()
		flat.sort()
		topk = flat[-k:]
		botk = flat[:k]
		M1 = topk - botk
		print "M1 =", M1
		## M2 ##
		ndimage.uniform_filter(conc, size = 3, mode = 'constant')		
#		plt.imshow(conc, cmap='YlOrRd', interpolation='nearest')
#		plt.show()
				
