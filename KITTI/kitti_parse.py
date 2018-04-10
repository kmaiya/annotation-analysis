import xml.etree.ElementTree as et
from xml.etree.ElementTree import ParseError
import os

NORMALIZED_WIDTH = 500.0
NORMALIZED_HEIGHT = 500.0
scaleX = NORMALIZED_WIDTH / 1392
scaleY = NORMALIZED_HEIGHT / 512

def getBBOXDimensions(xmin, ymin, xmax, ymax):
	coords = []
	coords.append(xmin)
	coords.append(ymin)
	coords.append(xmax - xmin)
	coords.append(ymax - ymin)
	return coords

def main():
	outFile1 = "kitti_ann"
	fileOut = open(outFile1, 'w')
	rootdir = './annotations/'
	imgId = 0
	typeList = ['Pedestrian', 'Person', 'Cyclist']
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			filepath = subdir + os.sep + file
			if filepath.endswith(".txt"):
				infile = open(filepath, 'r')
				imgId = filepath
				imgId = imgId.replace('./annotations//', '')
				imgId = imgId.replace('.txt', '')
				for line in infile:
					if any(x in line for x in typeList):
						annData = line.strip().split()
						xmin = float(annData[4])
						ymin = float(annData[5])
						xmax = float(annData[6])
						ymax = float(annData[7])
						dims = getBBOXDimensions(xmin, ymin, xmax, ymax)
						dims[0] = dims[0] * scaleX
						dims[1] = dims[1] * scaleY
						dims[2] = dims[2] * scaleX
						dims[3] = dims[3] * scaleY
						fileOut.write("%f %f %f %f %s\n" % (dims[0], dims[1], dims[2], dims[3], imgId))
			#imgId = imgId + 1

		
main()