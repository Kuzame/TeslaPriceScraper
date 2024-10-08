# USER INPUT HERE 

# ---------------- SETUP ---------------
#Indicate your Operating System: 'mac' for Apple/Macbook, 'win' for Windows
OperatingSystem = 'win'

#Locate your Google Chrome program
chromeLocationWin = "C:\Program Files\Google\Chrome Dev\Application\chrome.exe" #Edit if you're using Windows
chromeLocationMac = "/Applications/Google Chrome Dev.app" #Edit if you're using Mac

#(Windows Only) Locate your chromedriver.exe
chromedriverLocation = r'C:\temp\chromedriver.exe' #NOTE: Please leave the 'r' before strings of your chromedriver location!

#Enter your pushbullet API key. Obtained by: pushbullet.com > Settings > Account > Access Tokens, "Create Access Tokens"
PushBulletAPIkey = "o.test123-replace-with-your-key"

# ------------- CAR CONFIGURATION -----------
# Enter your model. 1 letter only: "S", "3", "X", "Y"
model = "Y"

# Enter your zip code
zipCode = 95132
zipCodeRange = 0 # Leave at 0 to search within your whole state by default currently, or 300 for 300 miles within your zip code for example

# Set the price threshold! The script will scrape the price below this number!
priceThreshold = 47500

# Set time range to re-search frequency. To reduce a chance of you getting blacklisted for DDOS-ing Tesla website
# For example, minTime = 60 and maxTime = 180 means it will re-search between 1-3 minutes
minTime = 60
maxTime = 180

# Tesla Trim:
# For model 3 or Y. Enter "M3AWD" or "MYRWD" for base model 3 or Y, "LRRWD" for long range RWD, "LRAWD" for long range AWD, "PAWD" for performance
model3orYTrim = "LRRWD"

# For model S. Enter "MSAWD" for base model S, "MSPLAID" for S Plaid
modelSTrim = "MSAWD"

# For model X. Enter "MXAWD" for base model X, "MXPLAID" for X Plaid
modelXTrim = "MXAWD"

# !Advanced config!
interiorColor3orY = "INTERIOR=PREMIUM_WHITE,PREMIUM_BLACK" # Options: INTERIOR=PREMIUM_WHITE,PREMIUM_BLACK . Select 1/multiple option, delete to blank "" for no preference
interiorColorSorX = "INTERIOR=CREAM,WHITE,BLACK" # Options: INTERIOR=CREAM,WHITE,BLACK . Select 1/multiple option, delete blank "" for no preference
# IF you need more advanced search, such as different multiple interior/exterior color, etc, carefully modify the whole link below

models = {
    "S": "https://www.tesla.com/inventory/new/ms?TRIM={}&{}&arrangeby=plh&zip={}&range={}".format(modelSTrim,interiorColorSorX, zipCode, zipCodeRange) ,
    "3": "https://www.tesla.com/inventory/new/m3?TRIM={}&{}&arrangeby=plh&zip={}&range={}".format(model3orYTrim,interiorColor3orY, zipCode, zipCodeRange) ,
    "X": "https://www.tesla.com/inventory/new/mx?TRIM={}&{}&arrangeby=plh&zip={}&range={}".format(modelXTrim,interiorColorSorX, zipCode, zipCodeRange) ,
    "Y": "https://www.tesla.com/inventory/new/my?TRIM={}&{}&arrangeby=plh&zip={}&range={}".format(model3orYTrim,interiorColor3orY, zipCode, zipCodeRange)
  # for example, if you want to replace "Y" below with black & white interior, replace the whole string & delete .format(zipCode) to be like below:
  # "Y": "https://www.tesla.com/inventory/new/my?TRIM=LRAWD&INTERIOR=PREMIUM_WHITE&arrangeby=plh&zip=95132&range=0"
}

