from planner.models import MealPlan
from datetime import datetime, timedelta, date
from django.core.exceptions import ObjectDoesNotExist

PLAN_DONE = 1
PLAN_STARTED = 2
PLAN_NOT_STARTED = 0


def getWeeks():
    now = datetime.now()
    monday = now - timedelta(days=now.weekday())
    seven_days = timedelta(7)
    fornight = timedelta(14)
    weeks = []
    current_week = monday.date()
    previous_week = current_week - seven_days

    meal_plan = check_week(previous_week)
    weeks.append(meal_plan)

    meal_plan = check_week(current_week)
    weeks.append(meal_plan)

    meal_plan = check_week(current_week + seven_days)
    weeks.append(meal_plan)

    meal_plan = check_week(current_week + fornight)
    weeks.append(meal_plan)

    print(weeks)

    return weeks


def check_week(date):
    meal_plan = {}
    meal_plan["start_of_week"] = date
    try:
        plan = MealPlan.objects.get(start_of_week=date)
        meal_plan["plan_state"] = plan.complete
    except ObjectDoesNotExist:
        plan = MealPlan(start_of_week=date, complete=PLAN_NOT_STARTED)
        plan.save()
        meal_plan["plan_state"] = PLAN_NOT_STARTED
    meal_plan["pk"] = plan.id
    return meal_plan
