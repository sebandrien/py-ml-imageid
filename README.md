# ml-imageid-py

This Python application utilizes a Caffe implementation of the Google MobileNet SSD detection network to detect and classify objects in a given image. The model is pretrained on VOC0712 with an mAP (mean Average Precision) of 0.727.

A minimum confidence threshold of 0.25 is applied to filter the detected objects. To maintain consistent classification colors, the seed "543210" is employed.

The chosen model is MobileNet-SSD. Upon detection, the application draws rectangles around the identified objects. In the top left corner of each rectangle, a confidence interval is displayed. The total number of detected objects is showcased in the bottom right of the image.
