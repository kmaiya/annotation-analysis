SAMPLE_SIZE = 589 # This is the smallest set of any given dataset collection

from random import shuffle

filenameList = ["./INRIA/inria_val_ann", "./INRIA/inria_train_ann", 
				"./KITTI/kitti_ann", "./COCO/coco_train_ann", 
				"./COCO/coco_val_ann", "./CAM2/cam2_ann", 
				"./SUN/sun_ann"]

for filename in filenameList:
	with open(filename, "r") as f:
		content = f.readlines()

	del content[0]
	#shuffle(content) #Do we want to shuffle or not?
	with open(filename + "_M3", "w") as f:
		areaSum = 0
		for x in range(0, len(content), SAMPLE_SIZE):
			if (x + SAMPLE_SIZE) < len(content):
				for y in range(x, SAMPLE_SIZE + x):
					currData = content[y].split()
					width = float(currData[2])
					height = float(currData[3])
					area = width * height
					areaSum += area
				avgArea = areaSum / SAMPLE_SIZE
				f.write("%f\n"  % avgArea)
