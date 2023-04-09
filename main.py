import numpy as np
import cv2

image_path = "roompeople.jpg"


np.random.seed(543210)
colors = np.random
min_confidence = 0.25

net = 

image = cv2.imread(image_path)
height, weight = 
blobl = 

net.setInput(blob)
detected_objects = net.foward()
