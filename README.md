# JasperModules
Custom Jasper Modules

##OpenCV Face Detect Module
This Jasper module uses OpenCV (Open Source Computer Vision) library and detect a Faces using USB Webcam, once a face is detected it then click a photo of that Face and save image in a user directory.<br />

Install OpenCV Lib<br />
```sudo apt-get install libopencv-dev python-opencv python-dev``` 

Also do following<br />
```cd ~```<br />
```mkdir out```<br />
```cd ~/jasper/static```<br />
```mkdir cascade```<br />
```cp haarcascade_frontalface_default.xml ~/jasper/static/cascade/.```<br />

You can use following Words for this module<br />
WORDS = ["HACK", "CAM", "WEBCAM", "PHOTO"]


##Currency Exchange Rate Calculator
This Jasper module uses Yahoo Finance Xchange Services. This module is specially design to use offline STT PocketSphinx efficiently. <br />

Install Semantic Lib<br />
```sudo pip install semantic``` 

You can use following Words for this module<br />
WORDS = ["CURRENCY", "EXCHANGE"]
