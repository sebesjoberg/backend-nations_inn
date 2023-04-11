from bs4 import BeautifulSoup
import dateparser
from datetime import datetime, timedelta


def eventScraper(data, browser):

    browser.get(data[0])
    soup = BeautifulSoup(browser.page_source, "lxml")

    title = soup.find_all('h1')

    time = soup.find_all("div", {"class": "item-date"})
    loc = soup.find_all("div", {"class": "item-organizer"})
    desc = soup.find_all("div", {"class": "p"})

    temp = []
    for detail in title:
        detail = str(detail.text)
        temp.append(detail)
    title = temp[0]
    if '-' in title:
        title = title.replace('-', ' ')
    temp = []
    for detail in time:
        detail = str(detail.text)
        temp.append(detail)
    time = temp[0]

    time = time.split(' - ')
    if time[0].find(':') == -1:
        time[0] = time[0]+':00'
    if time[1].find(':') == -1:
        time[1] = time[1]+':00'
    starttime = dateparser.parse(
        time[0], settings={'RETURN_AS_TIMEZONE_AWARE': False, 'DEFAULT_LANGUAGES': ["sv"]})
    endtime = dateparser.parse(
        time[1], settings={'RETURN_AS_TIMEZONE_AWARE': False, 'DEFAULT_LANGUAGES': ["sv"]})

    endtime = endtime.replace(
        year=starttime.year, month=starttime.month, day=starttime.day)
    if starttime > endtime:
        endtime = endtime + timedelta(days=1)
    time = [starttime, endtime]

    temp = []
    for detail in loc:
        detail = str(detail.text)
        temp.append(detail)
    loc = temp[0]

    temp = []
    for detail in desc:
        detail = str(detail.text)
        temp.append(detail)
    desc = temp[0]

    return title, time, loc, desc
