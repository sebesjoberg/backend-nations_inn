import smtplib
import ssl
import os
from .faceScraper import faceScraper as fs
from .nationScraper import nationScraper as ns
from .Dbdeleter import Dbdeleter as Dbd


def Dbpopulator():
    port = 587
    password = os.environ.get('MAILPASS')
    email = os.environ.get('VERIMAIL')

    email_reciever = os.environ.get('EMAIL_RECIEVER')
    event_list = []
    saved = 0
    notsaved = 0
    faulty_fc = 0
    faulty_ns = 0
    nationsguiden = False
    facebook = False
    facebook_events = []
    nationsguiden_events = []
    from ..models import Event, Nation
    try:
        nationsguiden_events = ns()
    except:
        nationsguiden = True
    try:
        facebook_events = fs()
    except:
        facebook = True
    for event in facebook_events:  # add faulty check here
        if event == None:
            faulty_fc += 1
        else:
            event_list.append(event)
    facebook_events = len(facebook_events)

    for event in nationsguiden_events:
        if event == None:
            faulty_ns += 1
        else:
            event_list.append(event)
    nationsguiden_events = len(nationsguiden_events)
    Dbd(nationsguiden_events > 0, facebook_events > 0)
    for event in event_list:
        if event == None:
            faulty = faulty+1
        else:
            e = Event()

            e.title = event[0]
            e.starttime = event[1]
            e.endtime = event[2]
            e.location = event[3]
            e.link = event[5]
            e.description = event[6]
            N = Nation.objects.get(name=event[4])
            e.nation = N
            e.logo = N.logo

            q = Event.objects.filter(nation=event[4])

            q = q.filter(title=event[0])

            q = q.filter(starttime__lte=event[1], endtime__gte=event[1])

            if q.exists():  # only one event check if it is and then replace it?? if not??
                q.delete()
                e.save()  # if event exist replaceS
                notsaved = notsaved+1

            else:
                e.save()

                saved = saved+1

    message = """Subject: Scraping report

    {total} were found, {saved} were saved, {notsaved} were not saved and {faulty_fc} facebook events were not scraped correctly, {faulty_ns} nationsguiden event were not scraped correctly.
    {nationsguiden} nationsguiden failed?, {facebook} facebook failed?. {nationsguiden_events} nationsguiden events, {facebook_events} facebook events"""
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    with smtplib.SMTP('smtp.office365.com', port) as server:
        server.starttls(context=context)
        server.login(email, password)
        server.sendmail(
            email,
            email_reciever,
            message.format(total=str(saved+notsaved+faulty_ns+faulty_fc), saved=str(saved),
                           notsaved=str(notsaved), faulty_fc=str(faulty_fc), faulty_ns=str(faulty_ns), facebook=str(facebook), nationsguiden=str(nationsguiden),
                           nationsguiden_events=str(nationsguiden_events), facebook_events=str(facebook_events))
        )
