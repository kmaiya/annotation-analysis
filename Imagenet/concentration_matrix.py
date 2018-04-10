import numpy as np 
import math
file = open("/Users/roopasree/Downloads/Annotation/ImageNet/annotations.txt","r") 
result = np.zeros((500,500))
for line in file:
	imageID,xmin,ymin,xmax,ymax,width,height = line.split(",")
	#imageID = int(imageID)

	xmin = int(float(xmin))
	xmax = int(float(xmax))
	ymin = int(float(ymin))
	ymax = int(float(ymax))
	width = int(float(width))
	height = int(float(height))
	width_new = xmax - xmin
	height_new= ymax-ymin
	temp = np.ones((width_new+1,height_new+1),dtype = int)
	result[xmin:xmax+1,ymin:ymax+1] = result[xmin:xmax+1,ymin:ymax+1] + temp
	#print(result)

print(result)