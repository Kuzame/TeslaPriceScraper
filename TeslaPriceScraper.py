# Please use my referral code if you find this program helpful in any way! =)
# Referral: https://ts.la/adrian371736
# Inventory referral, model:
# S: https://www.tesla.com/inventory/new/ms?arrangeby=plh&zip=95132&range=0&referral=adrian371736
# 3: https://www.tesla.com/inventory/new/m3?TRIM=LRAWD&arrangeby=plh&zip=95132&range=0&referral=adrian371736
# X: https://www.tesla.com/inventory/new/mx?arrangeby=plh&zip=95132&range=0&referral=adrian371736
# Y: https://www.tesla.com/inventory/new/my?TRIM=LRAWD&arrangeby=plh&zip=95132&range=0&referral=adrian371736

# ---------------------First Time Setup instructions-------------------
# 1. Install Google Chrome
# 2. Windows:
#    Download chromedriver (and extract it into folder. Note this location/place it into desired location!):
#       Check chrome version: Settings>About Chrome. For example, Version 118.0.5951.0 (Official Build) dev (64-bit). Note the "118" in this case.
#       Then go to https://chromedriver.chromium.org/downloads or https://googlechromelabs.github.io/chrome-for-testing/
#       Download "chromedriver" binary of win64 version 118... (for example).
#
#    Mac:
#    Install chromedriver using brew,
#       Install brew: https://sourabhbajaj.com/mac-setup/Homebrew/
#       Then: brew install --cask chromedriver
# 3. Install Python3 on your machine
#    +You need to pip install following libraries, enter the following on your command prompt/terminal:
#       pip3 install pushbullet.py
#       pip3 install beautifulsoup4
#       pip3 install selenium
#       pip3 install lxml
#       pip3 install webdriver-manager
# 4. Register for PushBullet account ( www.pushbullet.com ). Install pushbullet on your phone to get live notification.
#    Obtained pushbullet API key: pushbullet.com > Settings > Account > Access Tokens, "Create Access Tokens"
#    You will need this key for userinput.py file
# ---------------------------------------------------------------------

# ------------------------- How to use -----------------------------
# 1. After finished with "First Time Setup instructions", modify/customize your input on file "userinput.py".
# 2. For your convenience, you can view your result logs.history on carlist.txt/carlist-json.txt file that will be created in this same directory.
# Tips: Highly suggested that you have your browser Autofill ready, so you can purchase it in less than 1min the moment you get notification from here.
# ------------------------------------------------------------------


import json,pprint,time,threading,re,logging,random #,timechecker
from pushbullet import Pushbullet
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from userinput import OperatingSystem, chromeLocationWin, chromeLocationMac, chromedriverLocation, PushBulletAPIkey, model, zipCode, priceThreshold, minTime, maxTime, model3orYTrim, modelSTrim, modelXTrim, interiorColor3orY, interiorColorSorX, models

logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
logger.setLevel(logging.WARNING)
pb = Pushbullet(PushBulletAPIkey)
html = None


results_css_selector = 'div.results-container.results-container--grid.results-container--has-results'
delay, frequency = 10, 0
noCarFound=True
foundCarList=set()

#start_hour = 10
#end_hour = 19

while noCarFound:
    #timechecker.checkTime(start_hour,end_hour)
    try:
        frequency=random.randint(minTime, maxTime)
        print(datetime.now().strftime("%H:%M:%S") + " Searching Tesla Model " + model + " below $"+str(priceThreshold)+f", waiting {frequency}s")
        logging.basicConfig(level=logging.ERROR) 
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        agent = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("user-agent={0}".format(agent))
        service = Service(executable_path=chromedriverLocation)
        if OperatingSystem == 'mac':
            chrome_options.binary_location = chromeLocationMac
            browser = webdriver.Chrome(options=chrome_options)
        elif OperatingSystem == 'win':
            chrome_options.binary_location = chromeLocationWin
            browser = webdriver.Chrome(service=service, options=chrome_options)
        else:
            print("Please enter correct input for OperatingSystem (win/mac)")
            break
        browser.get(models[model])
        WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, results_css_selector))
        )

    except TimeoutException:
        print('Timeout Exception!')
    else:
        html = browser.page_source
    finally:
        browser.quit()

    if html:
        soup = BeautifulSoup(html, 'lxml')
        for car_html in soup.select_one(results_css_selector).findChildren('article'):
            car = {}
            car['price'] = int(re.sub('[^0-9]', '', car_html.select_one('section.result-header').select_one('div.result-pricing').select_one('span.result-purchase-price').text.replace('$', '').replace(',', '')))
            car['colour'] = car_html.select('section.result-features.features-grid')[0].select('ul')[1].select('li')[0].text
            car['type'] = car_html.select_one('section.result-header').select_one('div.result-basic-info').select_one('h3').text
            car['trim'] = car_html.select_one('section.result-header').select_one('div.result-basic-info').select('div')[0].text
            car['wheels'] = re.sub('[^0-9]', '', car_html.select('section.result-features.features-grid')[0].select('ul')[1].select('li')[1].text) + " inch wheels"
            car['interior'] = car_html.select('section.result-features.features-grid')[0].select('ul')[1].select('li')[2].text
            
            if car['price'] not in foundCarList:
                if(car['price'] < priceThreshold):
                    print(json.dumps(car))
                    push = pb.push_note(car['type']+" Tesla"+" - "+"$"+str(car['price']),car['trim']+" | "+car['colour']+" | "+car['interior'])
                    file1 = open("carlist.txt", "a")
                    file1.write("\n"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\n"+"$"+str(car['price'])+" "+car['trim']+" | "+car['colour']+" | "+car['interior']+"\n")
                    file1.close()
                    file2 = open("carlist-json.txt", "a")
                    file2.write("\n"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\n"+json.dumps(car)+"\n")
                    file2.close()

                    #######noCarFound=False
                    foundCarList.add(car['price'])
        time.sleep(frequency) # seconds
