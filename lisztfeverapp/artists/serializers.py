from rest_framework import serializers
from . import models

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Artists
        fields = '__all__'
