from django.db import models

departments = {
    "bsit": "BSIT",
    "bsme": "BSME"
}
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    department = models.CharField(max_length=200, choices=departments)
    
    class Meta:
        db_table = "student"