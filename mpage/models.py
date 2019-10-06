from django.db import models

# Create your models here.
class ModelTestDB(models.Model):
    ch1 = models.CharField(max_length=300)
    ch2 = models.CharField(max_length=300)
    int1 = models.IntegerField(null=True)