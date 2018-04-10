import xml.etree.ElementTree as et
from xml.etree.ElementTree import ParseError
import os

NORMALIZED_WIDTH = 500.0
NORMALIZED_HEIGHT = 500.0

def getBBOXDimensions(xmin, ymin, xmax, ymax):
	coords = []
	coords.append(xmin)
	coords.append(ymin)
	coords.append(xmax - xmin)
	coords.append(ymax - ymin)
	return coords

def main():
	outFile1 = "cam2_ann"
	fileOut = open(outFile1, 'w')
	rootdir = './annotations/'
	imgCount = 0
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			filepath = subdir + os.sep + file
			if filepath.endswith(".xml"):
				infile = filepath
				try:
					tree = et.parse(infile)
				except ParseError:
					print("Skipped: %s" % filepath)
				root = tree.getroot()
				width = int((root.find('size')).find('width').text)
				height = int((root.find('size')).find('height').text)
				for obj in root.findall('object'):
					xmin = int(obj.find('bndbox').find('xmin').text)
					xmax = int(obj.find('bndbox').find('xmax').text)
					ymin = int(obj.find('bndbox').find('ymin').text)
					ymax = int(obj.find('bndbox').find('ymax').text)
					dims = getBBOXDimensions(xmin, ymin, xmax, ymax)
					scaleX = NORMALIZED_WIDTH / width
					scaleY = NORMALIZED_HEIGHT / height
					dims[0] = dims[0] * scaleX
					dims[1] = dims[1] * scaleY
					dims[2] = dims[2] * scaleX
					dims[3] = dims[3] * scaleY
					fileOut.write("%f %f %f %f %s\n" % (dims[0], dims[1], dims[2], dims[3], root.find('filename').text))
			imgCount = imgCount + 1
	print(imgCount)

		
main()