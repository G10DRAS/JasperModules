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
WORDS = ["SELFIE", "CLICK", "SMILE", "PHOTO"]


##Currency Exchange Rate Calculator
This Jasper module uses Yahoo Finance Xchange Services. This module is specially design to use offline STT PocketSphinx efficiently. <br />

Install Semantic Lib<br />
```sudo pip install semantic``` 

You can use following Words for this module<br />
WORDS = ["CURRENCY", "EXCHANGE"]


##Twitter
Tweeter module to send tweets, get Notifications, get whats treanding for your city and get public tweets from Tweeter. <br />

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

```Send a tweet on tweeter```<br />

* To get twitter treands

```What's trending on tweeter```<br />

* To get tweeter notifications

```Get tweeter notifications```<br />

* To get public tweets

```Get tweets on twitter```<br />


##OpenWeatherMap Module
Get Current Weather Forecast, Weather Forecast for Next Week, Weather Forecast of Next Day. <br />
Coming soon.... <br />

##Tank Battle Game (FURRY)
Voice Controlled Tank Battle Game. Destroy Enemy Tank by controlling your FURRY with your voice. //===-- <br />
Coming soon.... <br />

![Alt text](https://github.com/G10DRAS/JasperModules/blob/master/TankGame.jpg "Tank Game")
