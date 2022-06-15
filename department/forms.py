from django import forms 
from mainapp.models import Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name','hod']