import pandas as pd
from bs4 import BeautifulSoup


def eventFinder(fb_page, browser):

    browser.get(fb_page)

    soup = BeautifulSoup(browser.page_source, "lxml")

    links = [a.get('href') for a in soup.find_all('a', href=True)]

    # finds all links on the page of interest
    df = pd.DataFrame(links)
    df.columns = ['Links']
    eventlinks = df['Links'].loc[df['Links'].str.startswith(
        '/events/', na=False)].to_list()
    eventlinks.pop(0)
    # filters out non event ones
    if len(eventlinks) == 0:
        print("noevents", fb_page)

    mbasic_links = []
    fb_links = []

    for event in eventlinks:
        if "/create/" not in event:
            mbasic = 'http://mbasic.facebook.com' + event
            fb = 'http://www.facebook.com' + event

            mbasic_links.append(mbasic)
            fb_links.append(fb)

    # creates the actual mbasic link and actual normal fb link
    return mbasic_links, fb_links
