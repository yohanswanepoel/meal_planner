from django import forms

from planner.models import MealPlan, Meal, Vegetable, Mains, Starch, Salad


class DayForm(forms.Form):
    day = forms.CharField()

    mains = forms.ModelChoiceField(
        label="Mains",
        queryset=Mains.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    veg = forms.ModelMultipleChoiceField(
        label="Vegies",
        queryset=Vegetable.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
    starch = forms.ModelMultipleChoiceField(
        label="Starch",
        queryset=Starch.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
    salad = forms.ModelMultipleChoiceField(
        label="Salad",
        queryset=Salad.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
