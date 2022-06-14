from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
class Hod(models.Model):
    name =  models.CharField(max_length=120)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
class Students(models.Model):
    GENDER = [("m","Male"),("f","Female")]
    admission_number = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    middle_name = models.CharField(max_length=120,blank=True)
    last_name = models.CharField(max_length=120)
    parent_name = models.CharField(max_length=120)
    address = models.TextField()
    number = models.IntegerField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    DOB = models.DateField()
    Joined_date = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=GENDER)

    def __str__(self):
        return self.first_name + " " + self.last_name