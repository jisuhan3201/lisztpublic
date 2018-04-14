from rest_framework import serializers
from . import models
from lisztfeverapp.events import serializers as event_serializers

class ArtistSerializer(serializers.ModelSerializer):

    artist_events = event_serializers.EventSerializer(many=True)

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
            "artist_events",
            "updatedat"
        )
