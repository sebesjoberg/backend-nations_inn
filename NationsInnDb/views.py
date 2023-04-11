
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

        if nation is not None:  # use Q object here to get for both nation and time
            queryset = queryset.filter(nation=nation)
        elif starttime is not None:
            starttime = starttime[:10]
            if starttime.find('/') != -1:
                starttime = starttime.split('/')
                if len(starttime[0]) != 4:
                    starttime = '20'+starttime[2] + \
                        '-'+starttime[0]+'-'+starttime[1]
                else:
                    starttime = starttime[2] + '-' + \
                        starttime[0]+'-'+starttime[1]
            criterion1 = Q(starttime__date=starttime)

            queryset = queryset.filter(
                criterion1)
        queryset = queryset.order_by('starttime')

        return queryset
