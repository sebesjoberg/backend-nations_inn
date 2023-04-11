from django.db.models.functions import Now


def Dbdeleter(ns, fc):
    from ..models import Event
    print(ns, fc)
    if(ns):
        # delete all nationsguiden if something whre scraped
        Event.objects.filter(link__icontains="nationsguiden").delete()

    if(fc):
        # delete all facebook if something whre scraped
        Event.objects.filter(link__icontains="facebook").delete()
    # end by removing thoose that have happened
    Event.objects.filter(endtime__lt=Now()).delete()
