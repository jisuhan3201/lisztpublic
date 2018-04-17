from rest_framework import serializers
from . import models
from lisztfeverapp.artists import serializers as artist_serializers
from lisztfeverapp.events import serializers as event_serializers

class PlanSerializer(serializers.ModelSerializer):

    event = event_serializers.EventSerializer()

    class Meta:
        model = models.Plan
        fields = (
            "id",
            "event",
            "created_at"
        )

class FollowArtistSerializer(serializers.ModelSerializer):

    artist = artist_serializers.ArtistSerializer()

    class Meta:
        model = models.FollowArtist
        fields = (
            "source",
            "classification",
            "artist",
            "created_at"
        )

class UserSerializer(serializers.ModelSerializer):

    user_plans = PlanSerializer(many=True)
    user_follow_artists = FollowArtistSerializer(many=True)

    class Meta:
        model = models.User
        fields = (
            'id',
            'name',
            "event_count",
            "following_count",
            'user_plans',
            'user_follow_artists',
        )

class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            "id",
            "username",
            "name",
            "first_name",
            "last_name",
            "email",
            "event_count",
            "following_count",                        
            "user_events",
            "following_artists"
        )
