from django.db import models

# Create your models here.

class ESGModel(models.Model):
    uid = models.CharField(max_length=100, null=True)
    data = models.CharField(max_length=100)

    def __str__(self):
        return self.uid