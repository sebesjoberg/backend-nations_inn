from rest_framework import serializers
from .models import Event, Nation


class NationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nation
        fields = ['id', 'name', 'description', 'facebook_Link', 'site_Link',
                  'latitude', 'longitude', 'address', 'logo', 'marker']


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'title', 'starttime', 'endtime',
                  'nation', 'location', 'link', 'description', 'logo']
