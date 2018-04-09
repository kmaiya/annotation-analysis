import json

NORMALIZED_WIDTH = 500.0
NORMALIZED_HEIGHT = 500.0
IMAGE_SIZE_STRING = 'Image size (X x Y x C)'
BBOX_STRING = 'Bounding box for object'

def getDimensions(line):
	dims = [int(s) for s in line.split() if s.isdigit()]
	del dims[2]
	return dims

def getBBOXDimensions(line):
	dims = [int(s) for s in line.replace('(', '').replace(')','').replace(',','').split() if s.isdigit()]
	del dims[0]
	coords = []
	coords.append(dims[0])
	coords.append(dims[1])
	coords.append(dims[2] - dims[0])
	coords.append(dims[3] - dims[1])
	return coords

def main():
	trainAnnsList = './annotations/Train/annotations.lst'
	testAnnsList = './annotations/Test/annotations.lst'
	outFile1 = './inria_train_ann'
	outFile2 = './inria_val_ann'

	width = 0
	height = 0
	imgId = 0
	trainOut = open(outFile1, 'w')
	trainOut.write('%d %d\n' % (NORMALIZED_WIDTH, NORMALIZED_HEIGHT))
	with open(trainAnnsList, 'r') as trainList:
		for trainDir in trainList:
			trainDir = trainDir.strip()
			imgId = trainDir
			imgId = imgId.replace('Train/annotations/', '')
			imgId = imgId.replace('.txt', '')
			with open('./annotations/' + trainDir, 'r') as inf:
				for line in inf:
					line = line.strip()
					if IMAGE_SIZE_STRING in line:
						[width, height] = getDimensions(line)
					elif BBOX_STRING in line:
						dims = getBBOXDimensions(line)
						scaleX = NORMALIZED_WIDTH / width
						scaleY = NORMALIZED_HEIGHT / height
						dims[0] = dims[0] * scaleX
						dims[1] = dims[1] * scaleY
						dims[2] = dims[2] * scaleX
						dims[3] = dims[3] * scaleY
						trainOut.write("%f %f %f %f %s\n" % (dims[0], dims[1], dims[2], dims[3], imgId))
			#imgId = imgId + 1
	trainOut.close()

	width = 0
	height = 0
	imgId = 0
	testOut = open(outFile2, 'w')
	testOut.write('%d %d\n' % (NORMALIZED_WIDTH, NORMALIZED_HEIGHT))
	with open(testAnnsList, 'r') as testList:
		for testDir in testList:
			testDir = testDir.strip()
			imgId = testDir
			imgId = imgId.replace('Test/annotations/', '')
			imgId = imgId.replace('.txt', '')
			with open('./annotations/' + testDir, 'r') as inf:
				for line in inf:
					line = line.strip()
					if IMAGE_SIZE_STRING in line:
						[width, height] = getDimensions(line)
					elif BBOX_STRING in line:
						dims = getBBOXDimensions(line)
						scaleX = NORMALIZED_WIDTH / width
						scaleY = NORMALIZED_HEIGHT / height
						dims[0] = dims[0] * scaleX
						dims[1] = dims[1] * scaleY
						dims[2] = dims[2] * scaleX
						dims[3] = dims[3] * scaleY
						testOut.write("%f %f %f %f %s\n" % (dims[0], dims[1], dims[2], dims[3], imgId))
			#imgId = imgId + 1
	testOut.close()
			
main()




