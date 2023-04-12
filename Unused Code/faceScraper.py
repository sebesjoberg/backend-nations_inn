from .CONFIG import pl, login, fbPages, names
from datetime import datetime
import os
from .eventFinder import eventFinder as ef
from .eventScraper import eventScraper as es
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import random
import time as t
[mail, password] = pl()
cookie_url = 'https://mbasic.facebook.com/cookie/consent_prompt/?next_uri=https%3A%2F%2Fmbasic.facebook.com%2F&refsrc=deprecated&_rdr'
POST_LOGIN_URL = login()
LINK_TO_FB_PAGE_OF_INTERESTS = fbPages()
NAMES = names()


def faceScraper():

    event_list = []
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')

    browser = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'),
                               options=chrome_options)
    browser.delete_all_cookies()

    browser.maximize_window()

    browser.get(cookie_url)
    try:
        cookie = browser.find_element(
            by=By.NAME, value="accept_only_essential")
        cookie.click()
    except:
        pass
    browser.get(POST_LOGIN_URL)

    username = browser.find_element(by=By.NAME, value="email")
    pwd = browser.find_element(by=By.NAME, value="pass")
    submit = browser.find_element(by=By.NAME, value="login")

    username.send_keys(mail)

    pwd.send_keys(password)
    k = 0
    submit.click()
    t.sleep(random.randint(1, 10))
    for i in range(len(LINK_TO_FB_PAGE_OF_INTERESTS)):
        [mbasic_links, fb_links] = ef(
            LINK_TO_FB_PAGE_OF_INTERESTS[i], browser)
        t.sleep(random.randint(1, 5))  # sleeps randomt ime to confuse
        k = k+len(mbasic_links)
        for m in range(len(mbasic_links)):

            mb = mbasic_links[m]
            try:
                [title, time, location, description] = es(
                    mb, browser, NAMES[i])

                if time[0] != None and time[1] != None:
                    event = [title, time[0], time[1],
                             location, NAMES[i], fb_links[m].split('?')[0], description]
                    event_list.append(event)
                else:
                    event_list.append(None)
            except:
                print("hello world", mb)
                event_list.append(None)
            # goes back to confuse fb
            browser.get(LINK_TO_FB_PAGE_OF_INTERESTS[i])
            t.sleep(random.randint(1, 5))  # sleeps random to confuse
    browser.close()

    return event_list
