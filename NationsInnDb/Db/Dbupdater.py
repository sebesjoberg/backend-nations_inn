from .nationScraper import nationScraper as ns
from .Dbdeleter import Dbdeleter


def Dbupdater():
    
    event_list = []
    fail = False
    from ..models import Event, Nation
    try:
        event_list = ns()
    except:
        print("failed")
        fail = True
    if None in event_list:
        Dbdeleter(fail or True)
        
    for event in event_list:
        
        try:
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

            q.delete()
            e.save()
        except:
            pass
    print("done")

                

   
