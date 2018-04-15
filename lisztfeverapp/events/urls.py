from django.urls import include, path  #django 2.0 version url dispatcher
from . import views

app_name = "events"
urlpatterns = [
    path("<str:event_id>/plan", view=views.PlanEvent.as_view(), name='plan_event'),
]
