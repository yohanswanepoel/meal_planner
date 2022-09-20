from django.shortcuts import render, redirect
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
    View,
    FormView,
    UpdateView,
)

# from meal_planner.planner.models import Meal, MealPlan

from planner.models import MealPlan, Meal, Vegetable, Mains, Starch
from .utils import getWeeks
from .forms import DayForm


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


class PlannerDetailView(View):
    template_name = "planner/plan_detail.html"
    model = MealPlan
    form_class = DayForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            # process form
            print(form)
            pass
        return redirect(reverse("planner:plan_view", args=[8]))

    def get(self, request, pk=None):
        # Define Forms
        monday_form = self.form_class()
        tuesday_form = self.form_class()
        wednesday_form = self.form_class()
        thursday_form = self.form_class()
        friday_form = self.form_class()
        saturday_form = self.form_class()
        sunday_form = self.form_class()
        context = {}
        meal_plan = get_object_or_404(MealPlan, pk=pk)
        context = {}
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

        context["monday_form"] = monday_form
        context["tuesday_form"] = tuesday_form
        context["wednesday_form"] = wednesday_form
        context["thursday_form"] = thursday_form
        context["friday_form"] = friday_form
        context["saturday_form"] = saturday_form
        context["sunday_form"] = sunday_form

        return render(request, self.template_name, context=context)


planner_update_view = PlannerUpdateView.as_view()
