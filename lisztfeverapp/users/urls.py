from django.conf.urls import url
from django.urls import include, path  #django 2.0 version url dispatcher
from . import views

app_name = "users"
urlpatterns = [
    path("", view=views.UserMain.as_view(), name='user'),
    path("all/", view = views.ListAllUsers.as_view(), name = 'all_users'),
    url(regex = r"^plans/$", view = views.ListAllPlans.as_view(), name = 'all_plans'),
    url(regex = r"^track_artists/$", view = views.ListAllTrackArtists.as_view(), name = 'all_track_artists'),
    url(regex=r"^$", view=views.UserListView.as_view(), name="list"),
    url(regex=r"^~redirect/$", view=views.UserRedirectView.as_view(), name="redirect"),
    url(regex=r"^~update/$", view=views.UserUpdateView.as_view(), name="update"),
    url(
        regex=r"^(?P<username>[\w.@+-]+)/$",
        view=views.UserDetailView.as_view(),
        name="detail",
    ),
]
