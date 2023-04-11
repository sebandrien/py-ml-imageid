import numpy as np
import cv2

image_path = "roompeople.jpg" #Define "image_path"
prototxt_path = 
model_path = 

min_confidence = 0.25 #Using a minimum confidence value of 0.25

classes = ["background", "aeroplane", "bicycle, "bottle", "bus", "cat", "chair", "person"]

np.random.seed(543210)
colors = np.random.uniform(0,255, size=(len(classes),3))

net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path) #Creating a neural network called net

image = cv2.imread(image_path)
height, width = image.shapre[0], image.shape[1]
blobl = cv2.dnn.blobFromImage(cv2.resize(image,(300,300)), 0.007, (300,300), 130)

net.setInput(blob)
detected_objects = net.foward()

for i in range(detected_objects[2])
 
  confiedence = int(detected_objects[0][0][i][2])
  
  if confidence > min_confidence:
   class_index = int(detected_objects[0,0,i,1])
  
   upper_left_x = int(detected_objects[0,0,i,3] * width)
   upper_left_y = int(detected_objects[0,0,i,4] * width)
   lower_right_x = int(detected_objects[0,0,i,5] * width)
   lower_right_y = int(detected_objects[0,0,i,6] * width)
  
   prediction_text = f"{classes[class_index]}: {confidence:.2f}%"
   cv2.rectangle(image, (upper_left_x, upper_left_y), (lower_right_x, lower_right_y))
   cv2.putText(image, prediction_text, upper_left_x, upper_left_y - 15 if upper_left_y > 30 else upper_left_y + 15, cv2.FONT_HERSHEY_SIMPLEX, 0.6, colors{class_index],2)
   
                                         
                                         

print(detected_objects[0][0][0][0])


cv2.imshow("Detected objects", image)
cv2.waitkey(0) #Continue executing on key press
cv2.destroyAllWindows() #Close all windows
