from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, ListView, View
from planner.models import MealPlan
from .utils import getWeeks


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
