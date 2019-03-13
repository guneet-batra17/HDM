from django.db import models

class Department(models.Model):
    department_id=models.AutoField(primary_key=True)
    department_name=models.CharField(max_length=225)
    department_strength=models.IntegerField()
    department_location=models.CharField(max_length=225)
    department_head=models.CharField(max_length=225)

# Create your models here.
