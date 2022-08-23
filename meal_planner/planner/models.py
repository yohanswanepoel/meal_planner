from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Mains(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(blank=True, default="")

    class Meta:
        app_label = "planner"

    def __str__(self):
        return self.name


class Salad(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        app_label = "planner"

    def __str__(self):
        return self.name


class Vegetable(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        app_label = "planner"

    def __str__(self):
        return self.name


class Starch(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        app_label = "planner"

    def __str__(self):
        return self.name


class Meal(models.Model):
    mains = models.ForeignKey(Mains, on_delete=models.DO_NOTHING)
    vegies = models.ManyToManyField(Vegetable)
    starches = models.ManyToManyField(Starch)
    salad = models.ManyToManyField(Salad)

    class Meta:
        app_label = "planner"

    def __str__(self) -> str:
        return self.mains


class MealPlan(models.Model):
    class Plan_State(models.IntegerChoices):
        PLAN_DONE = 1, _("Done")
        PLAN_STARTED = 2, _("Started")
        PLAN_NOT_STARTED = 0, _("Not Started")

    start_of_week = models.DateField()
    complete = models.IntegerField(
        choices=Plan_State.choices, default=Plan_State.PLAN_STARTED
    )
    day_monday = models.ForeignKey(
        Meal, related_name="fk_monday", blank=True, null=True, on_delete=models.CASCADE
    )
    day_tuesday = models.ForeignKey(
        Meal, related_name="fk_tuesday", blank=True, null=True, on_delete=models.CASCADE
    )
    day_wednesday = models.ForeignKey(
        Meal,
        related_name="fk_wednesday",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    day_thursday = models.ForeignKey(
        Meal,
        related_name="fk_thursday",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    day_friday = models.ForeignKey(
        Meal, related_name="fk_friday", blank=True, null=True, on_delete=models.CASCADE
    )
    day_saturday = models.ForeignKey(
        Meal,
        related_name="fk_saturday",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    day_sunday = models.ForeignKey(
        Meal, related_name="fk_sunday", blank=True, null=True, on_delete=models.CASCADE
    )

    class Meta:
        app_label = "planner"

    def __str__(self):
        return str(self.start_of_week)
