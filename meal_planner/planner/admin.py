from django.contrib import admin
from .models import Mains, Starch, Vegetable, Meal, MealPlan, Salad

# Register your models here.
admin.site.register(Mains)
admin.site.register(Starch)
admin.site.register(Vegetable)
admin.site.register(Salad)
admin.site.register(Meal)
admin.site.register(MealPlan)
