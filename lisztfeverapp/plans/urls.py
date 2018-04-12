from django.conf.urls import url
from . import views

app_name = "plans"
urlpatterns = [
    url(
        regex = r"^all/$",
        view = views.ListAllPlans.as_view(),
        name = 'all_plans'
    )

]
