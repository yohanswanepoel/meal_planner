from django.urls import path

from meal_planner.planner.views import (
    PlannerDetailView,
    PlannerListView,
    PlannerUpdateView,
)

app_name = "planner"
urlpatterns = [
    path("", PlannerListView.as_view(), name="index"),
    path("plan/<int:pk>", PlannerDetailView.as_view(), name="plan_view"),
    path("plan_update/<int:pk>", PlannerUpdateView.as_view(), name="plan_update"),
]
