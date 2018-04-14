from django.urls import include, path  #django 2.0 version url dispatcher
from . import views

app_name = "artists"
urlpatterns = [
    path("<str:artist_id>/follow", view=views.FollowArtist.as_view(), name='follow_artist'),
]
