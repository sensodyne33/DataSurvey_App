from django.db import models

# Create your models here.
class SurveyData(models.Model):
    name = models.CharField(max_length=80)
    