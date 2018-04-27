from django.urls import include, path  #django 2.0 version url dispatcher
from . import views

app_name = "artists"
urlpatterns = [
    path("search/", view=views.SearchArtist.as_view(), name='search_artist'),
    path("<str:artist_id>/", view=views.Artist.as_view(), name='artist'),
    path("<str:artist_id>/follow/", view=views.FollowArtist.as_view(), name='follow_artist'),
    path("<str:artist_id>/unfollow/", view=views.UnFollowArtist.as_view(), name='unfollow_artist'),
]
