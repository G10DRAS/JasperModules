# JasperModules
Custom Jasper Modules

##OpenCV Face Detect Module
This Jasper module uses OpenCV (Open Source Computer Vision) library and detect a Faces using USB Webcam, once a face is detected it then click a photo of that Face and save image in a user directory.

Need to install OpenCV Lib
sudo apt-get install libopencv-dev python-opencv python-dev 

Also do following
cd ~
mkdir out
cd ~/jasper/static
mkdir cascade
copy haarcascade_frontalface_default.xml to ~/jasper/static/cascade

You can use following Words for this module
WORDS = ["HACK", "CAM", "WEBCAM", "PHOTO"]
