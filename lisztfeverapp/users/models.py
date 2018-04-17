from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from lisztfeverapp.artists import models as artist_models
from lisztfeverapp.events import models as event_models


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_events = models.ManyToManyField(event_models.Event, through='Plan', related_name="user_events")
    following_artists = models.ManyToManyField(artist_models.Artists, through='followArtist', related_name="follow_artists")

    def __str__(self):
        return self.username

    @property
    def event_count(self):
        return self.user_events.all().count()

    @property
    def following_count(self):
        return self.following_artists.all().count()


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Plan(TimeStampedModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_plans') #Without related_name default is plan_set
    event = models.ForeignKey(event_models.Event, on_delete=models.PROTECT)

    class Meta:
        ordering = ['-created_at']

class FollowArtist(TimeStampedModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_follow_artists') #Without related_name default is followartist_set
    artist = models.ForeignKey(artist_models.Artists, on_delete=models.CASCADE)
    source = models.CharField(max_length=64, null=True)
    classification = models.CharField(max_length=64, null=True)
    follow = models.IntegerField(null=True)

    class Meta:
        ordering = ['-created_at']
