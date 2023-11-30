import cv2
import numpy as np

image_path = '999.jpg'
prototxt_path = 'MobileNetSSD_deploy.prototxt'
model_path = 'MobileNetSSD_deploy.caffemodel'

minimum_confidence = 0.20 # Define minimum confidence interval 

classes = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "ddiningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

np.random.seed(543210)
colors = np.random.uniform(0, 255, size=(len(classes), 3))

net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

image = cv2.imread(image_path)
height, width = image.shape[0], image.shape[1]

# Padding the image to be a square image
if width != height:
    diff = abs(width - height)
    if width > height:
        pad_top = diff // 2
        pad_bottom = diff - pad_top
        image = cv2.copyMakeBorder(image, top=pad_top, bottom=pad_bottom, left=0, right=0, borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0])
    else:
        pad_left = diff // 2
        pad_right = diff - pad_left
        image = cv2.copyMakeBorder(image, top=0, bottom=0, left=pad_left, right=pad_right, borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0])

# Then resize and normalize
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007, (300, 300), 130)

net.setInput(blob)
detected_objects = net.forward()

for i in range(detected_objects.shape[2]):
    confidence = detected_objects[0][0][i][2]

    if confidence > minimum_confidence:
        class_index = int(detected_objects[0, 0, i, 1])
        if class_index < len(classes):
            upper_left_x = int(detected_objects[0, 0, i, 3] * width)
            upper_left_y = int(detected_objects[0, 0, i, 4] * height)
            lower_right_x = int(detected_objects[0, 0, i, 5] * width)
            lower_right_y = int(detected_objects[0, 0, i, 6] * height)

            prediction_text = f"{classes[class_index]}: {confidence:.2f}%"

            cv2.rectangle(image, (upper_left_x, upper_left_y), (lower_right_x, lower_right_y), colors[class_index], 2)
            cv2.putText(image, prediction_text, (upper_left_x, upper_left_y - 15 if upper_left_y > 30 else upper_left_y + 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, colors[class_index], 2)

cv2.imshow("Object Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
