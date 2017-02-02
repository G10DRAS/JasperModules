# JasperModules
Custom Jasper Modules

##OpenCV Face Detect Module
This Jasper module uses OpenCV (Open Source Computer Vision) library and detect a Faces using USB Webcam, once a face is detected it then click a photo of that Face and save image in a user directory.<br />

Webcam: Logicool HD C270 (Other similar webcam will work)<br />

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

Dialog with Jasper<br />
```
YOU: JASPER
JASPER: High Beep
YOU: Start Currency Rate Calculator
JASPER: Low Beep
JASPER: First Currency?
YOU: American Dollar
JASPER: Second Currency?
YOU: Japanese Yen
JASPER: Getting exchange rate of USD against JPY
JASPER: It is approximately 106.15 JPY for 1 USD
JASPER: Do you want to continue?
YOU: YES/NO
```
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

To send a tweet

```Send a tweet on tweeter```<br />

To get twitter treands

```What's trending on tweeter```<br />

To get tweeter notifications

```Get tweeter notifications```<br />

To get public tweets

```Get tweets on twitter```<br />


##OpenWeatherMap Module
Get Current Weather Forecast, Weather Forecast for Next Week, Weather Forecast of Next Day. <br />

Install Semantic Lib<br />
```sudo pip install semantic``` 

Install pyowm (A Python wrapper around the OpenWeatherMap web API) <br />
```sudo pip install pyowm==3.5``` 

You can signup for a free API key [on the OWM website](https://home.openweathermap.org/users/sign_up)

profile.yml config for Open Weather Map module<br />

```
OpenWeatherMap:
   api_key: 'xxxxxxx646464564xxxxxxxxxx'
   city_name: 'Tokyo'
   country: 'JP'
   temp_unit: 'fahrenheit'       # 'kelvin', 'celsius' or 'fahrenheit' 
```

Use following phrases<br />

To get current weather report

```Hows weather today```<br />
```Get current forecast```<br />

To get next days weather report

```Hows weather tommorow```<br />
```Weather forecast for tommorow```<br />

To get weekly forecast

```Get weekly forecast```<br />

##Jasper Support Forum Posts
This Jasper module fetch top posts from Jasper Support Forum and speak out author and title of post.<br />

Use following phrases<br />
```
Check Jasper Support Forum Posts
See recent forum posts
Check the forum
```
##Speech Recognition Jukebox (SRJuke)
Play your favorite song by saying song title or play internet radio (JAZZ, BLUE, ROCK, POP...). <br />
Supported Voice Commands: PLAY, PAUSE, STOP, NEXT, PREV, SHUFFLE, PLAYALL, RESUME, PLAYLIST

Sample phrases are...<br />
```
Play Radio Jazz (Play Jazz Music on Internet Radio) 
Play Thriller by Michael Jackson (Play song Thriller)
Play David Guetta Discography (Play David Guetta Album)
Play Dangerous Moonwalker and Cheap Thrills (Play 3 selected songs back 2 back)
```
##Telegram Bot (Talk & Reply to Bot Users)
You as a Telegram Bot, listen to quiries from your bot users and reply or send answers to them by talking in to Mic.

Coming soon..... Stay tune....
