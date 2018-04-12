from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from lisztfeverapp.artists import models as artist_models

class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    track_artists = models.ManyToManyField(artist_models.Artists)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class TimeStampedModel(models.Model):

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# class UserArtists(TimeStampedModel):
#
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     artist_id = models.ForeignKey(artist_models.Artists)
    # artist_id = models.CharField(max_length=140)
    # artist_name = models.CharField(max_length=140)
