import string
from django.db import models


class register(models.Model):
    student_name=models.TextField(max_length=15)
    dob=models.DateField(null=True) 
    physics_marks=models.IntegerField(null=True)
    chemistry_marks=models.IntegerField(null=True)
    cs_marks=models.IntegerField(null=True)
    per=models.FloatField(null=True)
def  __str__(self):
    return self.student_name
