import os
from selenium import webdriver
from .eventFinder import eventFinder as ef
from .eventScraper import eventScraper as es
from .CONFIG import names, shortnames



from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager



def nationScraper():
    nations = names()
    shorts = shortnames()
    event_list = []
    #options = Options()
    #options.headless = True
    
    browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    
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


