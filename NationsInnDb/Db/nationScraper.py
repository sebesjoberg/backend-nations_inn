import os
from selenium import webdriver
from .eventFinder2 import eventFinder as ef
from .eventScraper2 import eventScraper as es
from .CONFIG import names, shortnames


def nationScraper():
    nations = names()
    shorts = shortnames()
    event_list = []
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')

    browser = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'),
                               options=chrome_options)

    event_datas = ef(browser)

    for data in event_datas:
        try:
            [title, time, location, description] = es(data, browser)
            correct = False
            for i in range(len(shorts)):
                if shorts[i] in location.lower():
                    nation = nations[i]
                    correct = True
            if time[0] is None or time[1] is None:
                correct = False
            if correct:
                event = [title, time[0], time[1], location,
                         nation, data[0], description]
            else:
                event = None

            event_list.append(event)

        except:
            event_list.append(None)
    browser.close()

    return event_list
