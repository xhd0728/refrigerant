from django.db import models


# Create your models here.
class Refrigerant(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    formula = models.CharField(max_length=64)
    molecular_weight = models.CharField(max_length=64)
    curve_data = models.JSONField(default=dict)
    type = models.CharField(max_length=64)
    safety_index = models.CharField(max_length=64)
    env_impact_index = models.CharField(max_length=64)
