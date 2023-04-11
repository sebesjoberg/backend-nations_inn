
from bs4 import BeautifulSoup

import dateparser


def eventScraper(event_page, browser, nation):
    browser.get(event_page)

    soup = BeautifulSoup(browser.page_source, "lxml")

    title = soup.find_all('h1')
    desc = soup.find_all(
        "div", {"id": "unit_id_886302548152152"})
    time_loc = soup.find_all('dt')

    temp = []
    for detail in title:  # for loop finds title, title is the last element
        detail = str(detail.text)
        if detail == 'Summary':
            pass
        else:
            temp.append(detail)

    title = temp[-1]

    if '-' in title:
        title = title.replace('-', ' ')

    temp = []

    for detail in time_loc:
        detail = str(detail.text)
        # gets the time string and location string, last index is loc first is time
        temp.append(detail)

    time = temp[0]

    try:
        if time.find(' – ') != -1:

            time = time.split(' – ', 1)
            # if time[0].find(':') == -1:
            #time[0] = time[0]+':00'
            # if time[1].find(':') == -1:
            #time[1] = time[1]+':00'
            starttime = dateparser.parse(
                time[0], settings={'RETURN_AS_TIMEZONE_AWARE': False,
                                   'PREFER_DATES_FROM': 'future'})
            endtime = dateparser.parse(
                time[1], settings={'RETURN_AS_TIMEZONE_AWARE': False,
                                   'PREFER_DATES_FROM': 'future'})
        elif time.find(' - ') != -1:

            time = time.split(' - ')
            # if time[0].find(':') == -1:
            #time[0] = time[0]+':00'
            # if time[1].find(':') == -1:
            #time[1] = time[1]+':00'
            starttime = dateparser.parse(
                time[0], settings={'RETURN_AS_TIMEZONE_AWARE': False,
                                   'PREFER_DATES_FROM': 'future'})
            endtime = dateparser.parse(
                time[1], settings={'RETURN_AS_TIMEZONE_AWARE': False,
                                   'PREFER_DATES_FROM': 'future'})
        elif time.find('–') != -1:

            time = time.split('–', 1)
            # if time[0].find(':') == -1:
            #time[0] = time[0]+':00'
            # if time[1].find(':') == -1:
            #time[1] = time[1]+':00'

            starttime = dateparser.parse(
                time[0], settings={'RETURN_AS_TIMEZONE_AWARE': False,
                                   'PREFER_DATES_FROM': 'future'})
            endtime = dateparser.parse(
                time[1], settings={'RETURN_AS_TIMEZONE_AWARE': False,
                                   'PREFER_DATES_FROM': 'future'})

    # gets all weird dates like 2 dates 18 may-5 may try removing the things in front and parsing rest
        elif time.find('-') != -1:

            time = time.split('-', 1)
            # if time[0].find(':') == -1:
            #time[0] = time[0]+':00'
            # if time[1].find(':') == -1:
            #time[1] = time[1]+':00'
            starttime = dateparser.parse(
                time[0], settings={'RETURN_AS_TIMEZONE_AWARE': False,
                                   'PREFER_DATES_FROM': 'future'})
            endtime = dateparser.parse(
                time[1], settings={'RETURN_AS_TIMEZONE_AWARE': False,
                                   'PREFER_DATES_FROM': 'future'})

        else:

            # if time.find(':') == -1:
            #time = time+':00'

            starttime = dateparser.parse(
                time, settings={'RETURN_AS_TIMEZONE_AWARE': False,
                                'PREFER_DATES_FROM': 'future'})
            endtime = starttime
    except:
        print('time is wrong', time, temp[0])

    # try statement if one is None both gets set to None
    try:
        if starttime > endtime:
            if starttime.hour > endtime.hour:
                endtime = endtime.replace(
                    day=starttime.day+1, month=starttime.month)
            else:
                endtime = endtime.replace(
                    day=starttime.day, month=starttime.month)
    except:
        # try if start is not None to do end=start if end is not none start=en
        print("time is wrong", time)
        starttime = None
        endtime = None

    time = [starttime, endtime]

    if len(temp) > 1:  # checks if there is a adress otherwise plugs in the nation
        loc = temp[1]
    else:
        loc = nation
    if loc.find("SE-7") != -1:  # checks if its just a postal code plug in the nation if it is
        loc = nation

    temp = []
    for detail in desc:
        detail = str(detail.text)
        temp.append(detail)

    desc = temp[0]

    desc = desc.replace('Details', '', 1)

    return title, time, loc, desc
