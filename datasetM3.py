SAMPLE_SIZE = 1237 # This is the smallest set of any given dataset collection

from random import shuffle

filenameList = ["./INRIA/inria_train_ann", 
				"./KITTI/kitti_ann", "./COCO/coco_train_ann", 
				"./CAM2/cam2_ann", "./SUN/sun_ann"]

for filename in filenameList:
	with open(filename, "r") as f:
		totalContent = f.readlines()

	with open(filename + "_M3", "w") as f:
		for x in range(0, 500):
			areaSum = 0
			shuffle(totalContent)
			content = totalContent[:SAMPLE_SIZE]
			for y in range(0, SAMPLE_SIZE):
				currData = content[y].split()
				width = float(currData[2])
				height = float(currData[3])
				area = width * height
				areaSum += area
			avgArea = areaSum / SAMPLE_SIZE
			f.write("%f\n"  % avgArea)
