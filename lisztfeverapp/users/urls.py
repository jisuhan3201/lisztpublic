from django.conf.urls import url
from django.urls import include, path  #django 2.0 version url dispatcher
from . import views

app_name = "users"
urlpatterns = [
    path("", view=views.UserMain.as_view(), name='main'),
    path("users/", view = views.ListAllUser.as_view(), name = 'all_users'),
    path("events/", view = views.UserEvent.as_view(), name = 'user_events'),
    path("plans/", view = views.UserPlan.as_view(), name = 'user_plans'),
    path("settings/", view = views.UserSetting.as_view(), name = 'user_events'),
    path('login/facebook/', view=views.FacebookLogin.as_view(), name='fb_login'),
]
