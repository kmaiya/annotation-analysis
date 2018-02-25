import json

PERSON = 1 
NORMALIZED_WIDTH = 500.0
NORMALIZED_HEIGHT = 500.0

def getAnnotationsByCatId(anns, catIdList):
	annSubset = []
	for ann in anns:
		if ann['category_id'] in catIdList:
			annSubset.append(ann)
	return annSubset

def getImageDataById(imgs, imgId):
	for img in imgs:
		if img['id'] == imgId:
			return img

def normalizeAndOutput(inFile, outFile):
	file = open(inFile, 'r')
	jd = json.load(file)
	file.close()

	imgs = jd['images']

	allAnns = jd['annotations']
	print("Total Annotations: " + str(len(jd['annotations'])))

	personAnns = getAnnotationsByCatId(allAnns, [PERSON])
	print("Person Annotations: " + str(len(personAnns)))

	file = open(outFile, 'w')
	file.write('%d %d\n' % (NORMALIZED_WIDTH, NORMALIZED_HEIGHT))
	count = 0
	for ann in personAnns:
		imgId = ann['image_id']
		imgData = getImageDataById(imgs, imgId)

		bbox = ann['bbox']
		bboxX = bbox[0]
		bboxY = bbox[1]
		bboxWidth = bbox[2]
		bboxHeight = bbox[3]
		width = imgData['width']
		height = imgData['height']
		scaleX = NORMALIZED_WIDTH / width
		scaleY = NORMALIZED_HEIGHT / height

		bboxX = bboxX * scaleX
		bboxY = bboxY * scaleY
		bboxWidth = bboxWidth * scaleX
		bboxHeight = bboxHeight * scaleY

		file.write('%f %f %f %f %s\n' % (bboxX, bboxY, bboxWidth, bboxHeight, imgId))
		count = count + 1
		if count % 1000 == 0:
			print(count)

	file.close()

def main():
	infile1 = './annotations/instances_val2014.json'
	infile2 = './annotations/instances_train2014.json'
	outFile1 = './val_analysisInput'
	outFile2 = './train_analysisInput'

	print("Validation Annotations:\n")
	normalizeAndOutput(infile1, outFile1)
	print("Training Annotations:\n")
	normalizeAndOutput(infile2, outFile2)
main()




