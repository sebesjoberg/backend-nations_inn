from django.db.models.functions import Now


def Dbdeleter(fail):
    from ..models import Event
    
    if(not fail):
        #delete all if correct scrape
        Event.objects.delete()
    # end by removing thoose that have happened
    Event.objects.filter(endtime__lt=Now()).delete()
