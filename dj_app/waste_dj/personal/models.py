from django.db import models


'''
# Create your models here.
Priority =[
    ("L","LOW"),("M","MEDIUM"),("H","HIGH")

]
class Question(models.Model):
    title           = models.CharField(max_length=50)
    question        = models.TextField(max_length=500)
    priority        = models.CharField(max_length=1,choices=Priority)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name        = "The Question"
        verbose_name_plural = "Peoples Questions"
'''