
from .models import Event, Nation
from .serializers import EventSerializer, NationSerializer
from rest_framework import viewsets

from rest_framework import filters
from django.db.models import Q


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class NationViewSet(viewsets.ModelViewSet):
    queryset = Nation.objects.all()
    serializer_class = NationSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id']


class EventList(viewsets.ReadOnlyModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        nation = self.request.GET.get('nation', None)
        starttime = self.request.GET.get(
            'starttime', None)
        id = self.request.GET.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            return queryset
        if nation is not None: 
            
            nation = nation.split(',')
            
            queryset = queryset.filter(nation__in=nation)
        if starttime is not None:
            starttime = starttime.split(",")
            for index in range(len(starttime)):
                time = starttime[index][:10]
                if time.find('/') != -1:
                    time = time.split('/')
                    if len(time[0]) != 4:
                        time = '20'+time[2] + \
                            '-'+time[0]+'-'+time[1]
                    else:
                        time = time[2] + '-' + \
                            time[0]+'-'+time[1]
                starttime[index] = time
            

            queryset = queryset.filter(starttime__date__in=starttime)
        queryset = queryset.order_by('starttime')

        return queryset
