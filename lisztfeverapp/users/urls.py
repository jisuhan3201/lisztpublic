from django.conf.urls import url
from django.urls import include, path  #django 2.0 version url dispatcher
from . import views

app_name = "users"
urlpatterns = [
    path("", view=views.UserMain.as_view(), name='user'),
    path("all/", view = views.ListAllUsers.as_view(), name = 'all_users'),
    path("events/", view = views.UserEvents.as_view(), name = 'user_events'),
]
