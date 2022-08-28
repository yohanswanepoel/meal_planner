from django import forms


class PlannerForm(forms.Form):
    name = forms.CharField()
