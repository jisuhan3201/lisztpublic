from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User #cookiecutter default
from . import models, serializers
from lisztfeverapp.events import serializers as event_serializers
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class UserMain(APIView):

    def get(self, request, format=None): #format=None is json format

        user_id = request.user.id
        user = models.User.objects.filter(id=user_id)
        serializer = serializers.UserSerializer(user, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class ListAllUser(APIView):

    def get(self, request, format=None):

        all_users = models.User.objects.all()
        serializer = serializers.ListUserSerializer(all_users, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class UserEvent(APIView):

    def get(self, request, format=None):

        user = request.user
        user_follow_artists = user.user_follow_artists.all()

        user_events = []
        for artist in user_follow_artists:

            events = artist.artist.artist_events.all()
            for event in events:
                if event != False:
                    user_events.append(event)

        serializer = event_serializers.EventSerializer(user_events, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class UserSetting(APIView):

    def get(self, request, format=None): #format=None is json format

        user_id = request.user.id
        user = models.User.objects.filter(id=user_id)
        serializer = serializers.UserSerializer(user, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
