from django.urls import include, path  #django 2.0 version url dispatcher
from . import views

app_name = "events"
urlpatterns = [
    path("<str:event_id>/", view=views.Event.as_view(), name='event'),
    path("<str:event_id>/plan/", view=views.PlanEvent.as_view(), name='plan_event'),
    path("<str:event_id>/unplan/", view=views.UnPlanEvent.as_view(), name='unplan_event'),
]
