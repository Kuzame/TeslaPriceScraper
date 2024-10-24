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
        chrome_options.add_experimental_option("excludeSwitches", ['enable-logging']) #double to single quotation 9/2/24
        agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36' #as of Chrome (dev) 9/2/24
        chrome_options.add_argument("--log-level=3") #added 9/2/24
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
            try:
                div_text = car_html.select_one('section.result-header').select_one('div.result-basic-info').select('div')[1].text
                # Look for numbers followed by "miles" in the text
                miles_match = re.search(r'(\d{1,3}(?:,\d{3})*)\s*miles', div_text)
                
                if miles_match:
                    # If miles are found, extract and remove the commas
                    car['miles'] = int(miles_match.group(1).replace(',', ''))
                else:
                    # If no miles found, it's the first format (just year)
                    car['miles'] = 0
            except (IndexError, AttributeError):
                car['miles'] = 0
            car['wheels'] = re.sub('[^0-9]', '', car_html.select('section.result-features.features-grid')[0].select('ul')[1].select('li')[1].text) + " inch wheels"
            car['interior'] = car_html.select('section.result-features.features-grid')[0].select('ul')[1].select('li')[2].text
            
            if car['price'] not in foundCarList:
                if(car['price'] < priceThreshold):
                    print(json.dumps(car))
                    # For cars with miles
                    if car['miles'] > 0:
                        push = pb.push_note(
                            car['type'] + " Tesla" + " - " + "$" + str(car['price']),
                            car['trim'] + " | " + car['colour'] + " | " + car['interior'] + " | " + f"{car['miles']:,} miles"
                        )
                    else:
                        push = pb.push_note(
                            car['type'] + " Tesla" + " - " + "$" + str(car['price']),
                            car['trim'] + " | " + car['colour'] + " | " + car['interior'] + " | New"
                        )
                    #push = pb2.push_note(car['type']+" Tesla"+" - "+"$"+str(car['price']),car['trim']+" | "+car['colour']+" | "+car['interior'])
                    file1 = open("carlist.txt", "a")
                    file1.write("\n"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\n"+"$"+str(car['price'])+" "+car['trim']+" | "+car['colour']+" | "+car['interior'] + " | " + f"{car['miles']:,} miles"+"\n")
                    file1.close()
                    file2 = open("carlist-json.txt", "a")
                    file2.write("\n"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\n"+json.dumps(car)+"\n")
                    file2.close()

                    #######noCarFound=False
                    foundCarList.add(car['price'])
        time.sleep(frequency) # seconds
