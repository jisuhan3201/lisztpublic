from rest_framework import serializers
from . import models

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Events
        fields = '__all__'
