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


##Twitter
This Tweeter module is to send tweets, get Notifications, get whats treanding for your city and get public tweets from Tweeter. <br />

Install Unidecode Lib<br />
```sudo pip install unidecode``` 

Install tweepy Lib<br />
```git clone git://github.com/tweepy/tweepy.git```

```cd tweepy```

```python setup.py install```

You can use following Words for this module<br />
WORDS = ["TWITTER"]

profile.yml config for twitter module<br />

* From https://apps.twitter.com get following KEYS by creating a twitter application.

```
twitter:
  # Access Level Read and write
  TW_CONSUMER_KEY: 'xxxxxxxxxxxxxxxxxxxx'
  TW_CONSUMER_SECRET: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
  TW_ACCESS_TOKEN: 'xxxxxxxx-xxxxxxxxxxxxxxxxxxxxx'
  TW_ACCESS_TOKEN_SECRET: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
  WOEID: '<WOEID for your city or area>' 
  ```

Use following phrases<br />

* To send a tweet

```Send a tweet on tweeter```

* To get twitter treands

```What's trending on tweeter```

* To get tweeter notifications

```Get tweeter notifications```

* To get public tweets

```Get tweets on twitter```
