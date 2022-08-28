from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
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

from planner.models import MealPlan, Meal, Vegetable
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


class PlannerDetailView(DetailView):
    template_name = "planner/plan_detail.html"
    model = MealPlan

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
        # print(meal_plan.__dict__)
        monday = {}
        monday["vegies"] = meal_plan.day_monday.vegies.all()
        monday["starches"] = meal_plan.day_monday.starches.all()
        monday["salad"] = meal_plan.day_monday.salad.all()
        tuesday = {}
        tuesday["vegies"] = meal_plan.day_tuesday.vegies.all()
        tuesday["starches"] = meal_plan.day_tuesday.starches.all()
        tuesday["salad"] = meal_plan.day_tuesday.salad.all()
        wednesday = {}
        wednesday["veggies"] = meal_plan.day_thursday.vegies.all()
        wednesday["starches"] = meal_plan.day_thursday.starches.all()
        wednesday["salad"] = meal_plan.day_thursday.salad.all()
        thursday = {}
        thursday["vegies"] = meal_plan.day_thursday.vegies.all()
        thursday["starches"] = meal_plan.day_thursday.starches.all()
        thursday["salad"] = meal_plan.day_thursday.salad.all()
        friday = {}
        friday["vegies"] = meal_plan.day_friday.vegies.all()
        friday["starches"] = meal_plan.day_friday.starches.all()
        friday["salad"] = meal_plan.day_friday.salad.all()
        saturday = {}
        saturday["vegies"] = meal_plan.day_saturday.vegies.all()
        saturday["starches"] = meal_plan.day_saturday.starches.all()
        saturday["salad"] = meal_plan.day_saturday.salad.all()
        sunday = {}
        sunday["vegies"] = meal_plan.day_sunday.vegies.all()
        sunday["starches"] = meal_plan.day_sunday.starches.all()
        sunday["salad"] = meal_plan.day_sunday.salad.all()
        context["monday"] = monday
        context["tuesday"] = tuesday
        context["wednesday"] = wednesday
        context["thursday"] = thursday
        context["friday"] = friday
        context["saturday"] = saturday
        context["sunday"] = sunday

        return context


planner_update_view = PlannerUpdateView.as_view()
