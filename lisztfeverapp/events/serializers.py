from rest_framework import serializers
from . import models

class VenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Venue
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):

    venue = VenueSerializer()

    class Meta:
        model = models.Event
        fields = (
            "eventid",
            "eventname",
            "eventstartlocaldate",
            "eventimageurl",
            "primaryeventurl",
            "eventstatus",
            "maxprice",
            "minprice",
            "venue"
        )
