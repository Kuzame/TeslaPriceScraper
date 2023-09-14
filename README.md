#
# About TeslaPriceScraper

*Note: Confirmed working as of September 2023*

Have you ever found yourself endlessly browsing the Tesla inventory, only to spot fleeting price drops that vanish before you can react? Have you wondered, "If only I had the time to monitor this all day, how much could I potentially save?" I was in the same boat, tirelessly searching for discounts. That's when a friend gave me a simple yet brilliant idea: **why not create a script to monitor the price for you?**

I'm excited to share this **TeslaPriceScraper** script with you! It's the result of countless hours of tinkering, fine-tuning, and finally, achieving success. Thanks to this script, I was able to secure MYLR $5,000+ inventory discount.

I hope this script helps you snag an amazing deal. If you find it valuable, please consider using my referral link below. Feel free to drop me a message on [Reddit](https://www.reddit.com/user/Kuzame) if you have any questions or if you happen to use my referral link! Happy savings!

**[Tesla Inventory Referral Link](https://www.tesla.com/inventory/new/my?arrangeby=plh&zip=95132&range=0&referral=adrian371736)** *(You'll probably need this inventory link ready in your browser if you use my script =D )*

[Tesla General Referral Link](https://ts.la/adrian371736)

#
# First Time Setup Instructions

1. **Install Google Chrome**
   
2. **Download/Install Chromedriver**

   **For Windows:**
   - Download chromedriver and extract it into a folder. Note this location and place it in your desired location.
   - Check your Chrome version by going to Settings > About Chrome. For example, Version 118.0.5951.0 (Official Build) dev (64-bit). Note the version number (e.g., "118" in this case).
   - Visit [chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) or [googlechromelabs.github.io/chrome-for-testing](https://googlechromelabs.github.io/chrome-for-testing/)
   - Download the "chromedriver" binary for the win64 version that corresponds to your Chrome version.

   **For Mac:**
   - Install chromedriver using Homebrew:
     - Homebrew installation instruction [sourabhbajaj.com/mac-setup/Homebrew/](https://sourabhbajaj.com/mac-setup/Homebrew/)
     - After that, run the following command:
     ```bash
     brew install --cask chromedriver
     ```

3. **Install Python3 on your Machine**

   - Download and install Python3 from [python.org/downloads](https://www.python.org/downloads/)

   After installing Python3, you need to install the following libraries. Open your command prompt or terminal and run the following commands:

   ```bash
   pip3 install pushbullet.py
   pip3 install beautifulsoup4
   pip3 install selenium
   pip3 install lxml
   pip3 install webdriver-manager
   ```
   
4. **Register for free PushBullet Account**

   - Visit [www.pushbullet.com](https://www.pushbullet.com) and create a free PushBullet account.
   - Install the PushBullet app on your mobile device to receive live notifications.
   - Obtain your PushBullet API key by following these steps:
     - Visit [www.pushbullet.com](https://www.pushbullet.com) Settings > Account > Access Tokens.
     - Click "Create Access Tokens" to generate your API key.
     - You will need this API key for the `userinput.py` file.
#
# How to Use

1. **First-Time Setup**: Start by following the "First Time Setup" instructions. Once completed, navigate to the "userinput.py" file. This is the only file you'll ever need to customize.

2. **Running the Script**:
   - Open your Command Prompt or Terminal.
   - Use the `cd` command to navigate to the directory where you've placed these files.
   - Run the script with Python 3 using the following command:
     ```bash
     python3 TeslaPriceScraper.py
     ```

   Alternatively, you can simply right-click the "TeslaPriceScraper.py" file in your folder and select "Run with Python".

3. **Viewing Results**:
   - Your result and log history will be saved in "carlist.txt" and "carlist-json.txt" files in the same working directory for your convenience.

4. **Tips for Quick Purchases**:
   - I recommend having your browser's autofill feature ready to go. This way, you can make a purchase in less than a minute as soon as you receive a notification from this script.

#
