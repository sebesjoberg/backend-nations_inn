import pandas as pd
from bs4 import BeautifulSoup
import os
import time
from selenium.webdriver.common.by import By


DAYS_AHEAD = int(os.environ.get('DAYS_AHEAD'))


def eventFinder(browser):
    all_links = []
    browser.get('https://nationsguiden.se')
    for i in range(DAYS_AHEAD):
        soup = BeautifulSoup(browser.page_source, "lxml")

        links = [a.get('href') for a in soup.find_all('a', href=True)]

        # finds all links on the page of interest
        df = pd.DataFrame(links)
        df.columns = ['Links']
        eventlinks = df['Links'].loc[df['Links'].str.contains(
            'evid=', na=False)].to_list()
        # filters out non event ones

        for event in eventlinks:
            link = 'https://nationsguiden.se' + event
            if link in all_links:
                print("notappended")
            else:
                link = [link, i]
                all_links.append(link)

        next = browser.find_element(by=By.ID, value='datepicker-after-9018')
        next.click()

        time.sleep(5)

    return all_links
