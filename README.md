
# Shrek's bloxflip crash notifier

This supposedly works on a bold claim made by an user.

The way it works is fairly easy: It will notify you if the last crash multipliers were over x and y times in a row.

## Deployment

### Set your user agent
Open main.py and on line 14 customise the string with your user agent      
https://www.whatsmyua.info


### Install chromedriver
You need to install a chromedriver for this to work.
Head over to https://chromedriver.chromium.org and download the correct driver (Determined by your chrome version)


### Deploy
To install dependencies run
```bash
  python3 -m pip install -r requirements.txt
```
To start the checker run
```bash
  python3 main.py
```


## Demo

https://streamable.com/y7o4kr


## Customising the notification audio

Simply replace the notification.waw with another file. It needs to be named `notification.waw`

## Contributing

Contributions are always welcome!
