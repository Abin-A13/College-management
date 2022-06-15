from django import forms
from .models import Students

# this form is only for update the student data
# this are the fields we can update


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = [
            'first_name',
            'last_name',
            'parent_name',
            'number',
            'department',
            'address',
        ]
