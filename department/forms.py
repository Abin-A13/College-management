from django import forms 
from mainapp.models import Department

# This form is for Create and delete

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name','hod']