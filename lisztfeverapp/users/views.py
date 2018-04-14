from django.contrib.auth.mixins import LoginRequiredMixin #cookiecutter default
from django.urls import reverse #cookiecutter default
from django.views.generic import DetailView, ListView, RedirectView, UpdateView #cookiecutter default
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User #cookiecutter default
from . import models, serializers
from lisztfeverapp.events import serializers as event_serializers

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ["name"]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"

################################################################################

class UserMain(APIView):

    def get(self, request, format=None): #format=None is json format

        user_id = request.user.id
        user = models.User.objects.filter(id=user_id)
        serializer = serializers.UserSerializer(user, many=True)

        return Response(data=serializer.data)

class ListAllUsers(APIView):

    def get(self, request, format=None):

        all_users = models.User.objects.all()
        serializer = serializers.UserSerializer(all_users, many=True)

        return Response(data=serializer.data)

class UserEvents(APIView):

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

        return Response(data=serializer.data)

class ListAllPlans(APIView):

    def get(self, request, format=None):

        all_plans = models.Plan.objects.all()
        serializer = serializers.PlanSerializer(all_plans, many=True)

        return Response(data=serializer.data)

class ListAllFollowArtists(APIView):

    def get(self, request, format=None):

        all_follow_artists = models.FollowArtist.objects.all()
        serializer = serializers.FollowArtistSerializer(all_follow_artists, many=True)

        return Response(data=serializer.data)
