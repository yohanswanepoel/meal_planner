from django.urls import path

from meal_planner.planner.views import PlannerListView

app_name = "planner"
urlpatterns = [
    path("", PlannerListView.as_view(), name="index"),
]
