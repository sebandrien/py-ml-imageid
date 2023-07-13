# ml-imageid-py

A Python application that detects, classfies, and provides a confidence interval for a given image. The model used is a Caffe implementation of Google MobileNet SSD detection network, with pretrained weights on VOC0712 and mAP=0.727.

A minimum confidence interval of 0.25 is used.

The seed "543210" is used to keep the classification colors consistent.

The model used is - MobileNet-SSD.

In the bottom right of the image, the number of objects detected is displayed.

The application draws a rectangle over detected objects, on the top left, a confidence interval is displayed.
