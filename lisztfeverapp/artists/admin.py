from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.ArtistEvent)
class ArtistEventAdmin(admin.ModelAdmin):

    list_display = (
        "artist",
        "event",
        "created_at",
        "updated_at"
    )
