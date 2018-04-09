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
	outFile1 = "sun_ann"
	fileOut = open(outFile1, 'w')
	fileOut.write('%d %d\n' % (NORMALIZED_WIDTH, NORMALIZED_HEIGHT))
	rootdir = './annotations/'
	imgId = 0
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			filepath = subdir + os.sep + file
			if filepath.endswith(".xml"):
				infile = filepath
				imgId = filepath
				imgId = imgId.replace('.xml', '')
				imgId = imgId.replace('./annotations/', '')
				try:
					tree = et.parse(infile)
				except ParseError:
					print("Skipped: %s" % filepath)
				root = tree.getroot()
				if root.find('imagesize') is not None:
					width = int((root.find('imagesize')).find('ncols').text)
					height = int((root.find('imagesize')).find('nrows').text)
					for obj in root.findall('object'):
						if 'person' in obj.find('name').text:
							for polygon in obj.findall('polygon'):
								x = []
								y = []
								for pt in polygon.findall('pt'):
									x.append(int(pt.find('x').text))
									y.append(int(pt.find('y').text))
								xmin = min(x)
								xmax = max(x)
								ymin = min(y)
								ymax = max(y)
								dims = getBBOXDimensions(xmin, ymin, xmax, ymax)
								scaleX = NORMALIZED_WIDTH / width
								scaleY = NORMALIZED_HEIGHT / height
								dims[0] = dims[0] * scaleX
								dims[1] = dims[1] * scaleY
								dims[2] = dims[2] * scaleX
								dims[3] = dims[3] * scaleY
								fileOut.write("%f %f %f %f %s\n" % (dims[0], dims[1], dims[2], dims[3], imgId))
				#imgId = imgId + 1

		
main()