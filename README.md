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
```copy haarcascade_frontalface_default.xml to ~/jasper/static/cascade```<br />

You can use following Words for this module<br />
WORDS = ["HACK", "CAM", "WEBCAM", "PHOTO"]
