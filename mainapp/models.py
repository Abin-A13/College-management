from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=120)
    hod = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Students(models.Model):
    GENDER_CHOICES = (("m", "Male"), ("f", "Female"))
    admission_number = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    middle_name = models.CharField(max_length=120, blank=True)
    last_name = models.CharField(max_length=120)
    parent_name = models.CharField(max_length=120)
    address = models.TextField()
    number = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    DOB = models.DateField()
    Joined_date = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.first_name + " " + self.last_name
