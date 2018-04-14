from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from lisztfeverapp.artists import models as artist_models
from lisztfeverapp.events import models as event_models


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_events = models.ManyToManyField(event_models.Events, through='Plan', related_name="user_events")
    track_artists = models.ManyToManyField(artist_models.Artists, through='TrackArtist', related_name="track_artists")

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Plan(TimeStampedModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_plans') #Without related_name default is plan_set
    event = models.ForeignKey(event_models.Events, on_delete=models.PROTECT)
    status = models.CharField(max_length=64)

    class Meta:
        ordering = ['-created_at']

class TrackArtist(TimeStampedModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_track_artists') #Without related_name default is trackartist_set
    artist = models.ForeignKey(artist_models.Artists, on_delete=models.CASCADE)
    status = models.CharField(max_length=64)

    class Meta:
        ordering = ['-created_at']
