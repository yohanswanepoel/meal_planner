from django import forms

from planner.models import MealPlan, Meal, Vegetable, Mains, Starch, Salad


class PlannerForm(forms.Form):
    mains_monday = forms.ModelChoiceField(
        label="Mains",
        queryset=Mains.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    veg_monday = forms.ModelMultipleChoiceField(
        label="Vegies",
        queryset=Vegetable.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
    starch_monday = forms.ModelMultipleChoiceField(
        label="Starch",
        queryset=Starch.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
    salad_monday = forms.ModelMultipleChoiceField(
        label="Salad",
        queryset=Salad.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )

    mains_tuesday = forms.ModelChoiceField(
        label="Mains",
        queryset=Mains.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    veg_tuesday = forms.ModelMultipleChoiceField(
        label="Vegies",
        queryset=Vegetable.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
    starch_tuesday = forms.ModelMultipleChoiceField(
        label="Starch",
        queryset=Starch.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
    salad_tuesday = forms.ModelMultipleChoiceField(
        label="Salad",
        queryset=Salad.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )

    mains_wednesday = forms.ModelChoiceField(
        label="Mains",
        queryset=Mains.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    veg_wednesday = forms.ModelMultipleChoiceField(
        label="Vegies",
        queryset=Vegetable.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
    starch_wednesday = forms.ModelMultipleChoiceField(
        label="Starch",
        queryset=Starch.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
    salad_wednesday = forms.ModelMultipleChoiceField(
        label="Salad",
        queryset=Salad.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )

    mains_thursday = forms.ModelChoiceField(
        label="Mains",
        queryset=Mains.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    veg_thursday = forms.ModelMultipleChoiceField(
        label="Vegies",
        queryset=Vegetable.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
    starch_thursday = forms.ModelMultipleChoiceField(
        label="Starch",
        queryset=Starch.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
    salad_thursday = forms.ModelMultipleChoiceField(
        label="Salad",
        queryset=Salad.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )

    mains_friday = forms.ModelChoiceField(
        label="Mains",
        queryset=Mains.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    veg_friday = forms.ModelMultipleChoiceField(
        label="Vegies",
        queryset=Vegetable.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
    starch_friday = forms.ModelMultipleChoiceField(
        label="Starch",
        queryset=Starch.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
    salad_friday = forms.ModelMultipleChoiceField(
        label="Salad",
        queryset=Salad.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )

    mains_saturday = forms.ModelChoiceField(
        label="Mains",
        queryset=Mains.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    veg_saturday = forms.ModelMultipleChoiceField(
        label="Vegies",
        queryset=Vegetable.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
    starch_saturday = forms.ModelMultipleChoiceField(
        label="Starch",
        queryset=Starch.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
    salad_saturday = forms.ModelMultipleChoiceField(
        label="Salad",
        queryset=Salad.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )

    mains_sunday = forms.ModelChoiceField(
        label="Mains",
        queryset=Mains.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    veg_sunday = forms.ModelMultipleChoiceField(
        label="Vegies",
        queryset=Vegetable.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
    starch_sunday = forms.ModelMultipleChoiceField(
        label="Starch",
        queryset=Starch.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
    salad_sunday = forms.ModelMultipleChoiceField(
        label="Salad",
        queryset=Salad.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
