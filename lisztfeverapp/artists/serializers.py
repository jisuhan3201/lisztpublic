from rest_framework import serializers
from . import models
from lisztfeverapp.events import serializers as event_serializers

class ArtistSerializer(serializers.ModelSerializer):

    events = event_serializers.EventSerializer(many=True)

    class Meta:
        model = models.Artists
        fields = (
            "artistid",
            "artistname",
            "imageurl",
            "events",
        )

class SmallArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Artists
        fields = (
            "artistid",
            "artistname",
            "imageurl",
        )

class ArtistAllSerializer(serializers.ModelSerializer):

    events = event_serializers.EventSerializer(many=True)

    class Meta:
        model = models.Artists
        fields = (
            "artistid",
            "artistname",
            "attractionid",
            "popularity",
            "followers",
            "externalurl",
            "imageurl",
            "updatedat",
            "events",
        )
