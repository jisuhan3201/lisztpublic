from django.db import models
from lisztfeverapp.users import models as user_models
from lisztfeverapp.events import models as event_models

# Create your models here.
class TimeStampedModel(models.Model):

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Plan(TimeStampedModel):

    creator = models.OneToOneField(user_models.User, on_delete=models.CASCADE)
    event_id = models.CharField(max_length=64, null=True)
    event_name = models.CharField(max_length=255, null=True)
    event_image_url = models.URLField(max_length=255, null=True)
    event_start_local_date = models.DateField(max_length=64, null=True)
    event_start_local_time = models.TimeField(max_length=64, null=True)
    venue_id = models.CharField(max_length=64, null=True)
    venue_city = models.CharField(max_length=64, null=True)
    venue_street = models.CharField(max_length=64, null=True)
    venue_name = models.CharField(max_length=255, null=True)
    venue_lat = models.FloatField(null=True)
    venue_lng = models.FloatField(null=True)
