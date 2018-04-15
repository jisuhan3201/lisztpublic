from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from lisztfeverapp.users import models as user_models
# Create your views here.

class FollowArtist(APIView):

    def post(self, request, artist_id, format=None):

        user = request.user

        try:
            found_artist = models.Artists.objects.get(artistid=artist_id)
        except models.Artists.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisting_follow = user_models.FollowArtist.objects.get(
                user=user,
                artist=found_artist,
                source="webapp",
                classification="explore",
                follow=1
            )
            return Response(status=status.HTTP_304_NOT_MODIFIED)

        except user_models.FollowArtist.DoesNotExist:

            new_follow = user_models.FollowArtist.objects.create(
                user=user,
                artist=found_artist,
                source="webapp",
                classification="explore",
                follow=1
            )
            new_follow.save()

            return Response(status=status.HTTP_201_CREATED)

class UnFollowArtist(APIView):

    def delete(self, request, artist_id, format=None):

        user=request.user

        try:
            found_artist = models.Artists.objects.get(artistid=artist_id)
        except models.Artists.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisting_follow = user_models.FollowArtist.objects.get(
                user=user,
                artist=found_artist,
                source="webapp",
                classification="explore",
                follow=1
            )
            preexisting_follow.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except user_models.FollowArtist.DoesNotExist:

            return Response(status=status.HTTP_304_NOT_MODIFIED)
