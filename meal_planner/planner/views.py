from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    DetailView,
    RedirectView,
    ListView,
    FormView,
    UpdateView,
)

# from meal_planner.planner.models import Meal, MealPlan

from planner.models import MealPlan, Meal, Vegetable, Mains, Starch
from .utils import getWeeks
from .forms import PlannerForm


def index(request):
    return HttpResponse("Hello world!")


User = get_user_model()


# class PlannerListView(LoginRequiredMixin, ListView):
class PlannerListView(ListView):
    template_name = "planner/weeks.html"
    context_object_name = "plans"

    def get_queryset(self):
        """Return the last five published questions."""
        print("Get Query Set")
        return getWeeks()


class PlannerUpdateView(UpdateView):
    template_name = "planner/plan.html"
    context_object_name = "plans"
    model = MealPlan
    fields = "__all__"
    success = "#"


class PlannerDetailView(FormMixin, DetailView):
    template_name = "planner/plan_detail.html"
    model = MealPlan
    form_class = PlannerForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meal_plan = get_object_or_404(MealPlan, pk=self.kwargs["pk"])
        if meal_plan.day_monday is None:
            meal = Meal()
            meal.save()
            meal_plan.day_monday = meal
        if meal_plan.day_tuesday is None:
            meal = Meal()
            meal.save()
            meal_plan.day_tuesday = meal
        if meal_plan.day_wednesday is None:
            meal = Meal()
            meal.save()
            meal_plan.day_wednesday = meal
        if meal_plan.day_thursday is None:
            meal = Meal()
            meal.save()
            meal_plan.day_thursday = meal
        if meal_plan.day_friday is None:
            meal = Meal()
            meal.save()
            meal_plan.day_friday = meal
        if meal_plan.day_saturday is None:
            meal = Meal()
            meal.save()
            meal_plan.day_saturday = meal
        if meal_plan.day_sunday is None:
            meal = Meal()
            meal.save()
            meal_plan.day_sunday = meal
        meal_plan.save()

        context["meal_plan"] = meal_plan
        # Load meals as drop down
        mains = Mains.objects.filter()
        context["mains"] = mains

        vegie = Vegetable.objects.filter()
        context["vegetables"] = vegie

        starch = Starch.objects.filter()
        context["starch"] = starch

        return context


planner_update_view = PlannerUpdateView.as_view()
