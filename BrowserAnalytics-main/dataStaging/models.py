from django.db import models

# Create your models here.

class stagedflatfile(models.Model):
    a=models.TextField()
    b=models.TextField()
    c = models.TextField()

class flatfile(models.Model):
    fileName=models.TextField()
    flatFile=models.TextField()



