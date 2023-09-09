#
# TeslaPriceScraper 
*Note: Confirmed working as of September 2023*
### Get the lowest Tesla inventory price by using this Tesla Price Scraper python script

Please consider using my referral link if you find this script helpful in any way! =)

##### Referral link: https://ts.la/adrian371736
#### Inventory link referral:
Model **S** : https://www.tesla.com/inventory/new/ms?arrangeby=plh&zip=95132&range=0&referral=adrian371736

Model **3** : https://www.tesla.com/inventory/new/m3?arrangeby=plh&zip=95132&range=0&referral=adrian371736

Model **X** : https://www.tesla.com/inventory/new/mx?arrangeby=plh&zip=95132&range=0&referral=adrian371736

Model **Y** : https://www.tesla.com/inventory/new/my?arrangeby=plh&zip=95132&range=0&referral=adrian371736

#
# First Time Setup instructions
#### 1. Install Google Chrome
#### 2. Download/Install Chromedriver
#### Windows:

   Download chromedriver (and extract it into folder. Note this location/place it into desired location!):

   Check chrome version: Settings>About Chrome. For example, Version 118.0.5951.0 (Official Build) dev (64-bit). Note the "118" in this case.

   Then go to https://chromedriver.chromium.org/downloads or https://googlechromelabs.github.io/chrome-for-testing/

   Download "chromedriver" binary of win64 version 118... (for example).

####   Mac:

   Install chromedriver using brew,

   Install brew: https://sourabhbajaj.com/mac-setup/Homebrew/ . After that,

      brew install --cask chromedriver
#### 3. Install Python3 on your machine (such as https://www.python.org/downloads/ )

   After installing Python3, you need to pip install following libraries, enter the following on your command prompt/terminal:

      pip3 install pushbullet.py

      pip3 install beautifulsoup4

      pip3 install selenium

      pip3 install lxml

      pip3 install webdriver-manager
#### 4. Register for PushBullet account ( www.pushbullet.com ). Install pushbullet on your phone to get live notification.

   Obtained pushbullet API key: www.pushbullet.com > Settings > Account > Access Tokens, "Create Access Tokens"
   
   You will need this key for userinput.py file

#
# How to use 
1. After finished with "First Time Setup instructions", modify/customize your input on file "userinput.py". This is the only file you ever need to modify.
2. In case you don't know how to run the python, you can either (Assuming you are done with userinput as well)
   
   On Command Prompt/Terminal, cd (change directory) into where you put these files, then input:
      ```
      python3 TeslaPriceScraper.py
      ```
   or right click the TeslaPriceScraper.py file on the folder, and run with Python (program that you installed)
4. For your convenience, you can view your result/logs history on carlist.txt/carlist-json.txt file that will be created in your same working directory.
5. Tips: Highly suggested that you have your browser Autofill ready, so you can purchase it in less than 1min the moment you get notification from here.
#
