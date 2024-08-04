from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(required=False)

class Goal(models.Model):
    target = models.FloatField()
    complete = models.BooleanField()

class Spend(models.Model):
    day = models.DateField(auto_now_add=True)
    how_much = models.FloatField()
    accordingly = models.BooleanField()

class Calculate(models.Model):
    have_to_spend = models.FloatField()
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    daily_spend = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class Historic(models.Model):
    ...
