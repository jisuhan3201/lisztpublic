from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Plan)
class PlanAdmin(admin.ModelAdmin):

    list_display = (
        "creator",
        "event_id",
        "event_name",
        "event_image_url",
        "event_start_local_date",
        "event_start_local_time",
        "venue_id",
        "venue_city",
        "venue_street",
        "venue_name",
        "venue_lat",
        "venue_lng",
        "create_at",
        "updated_at",
    )
