from .models import Students
import django_filters

class StudentFilter(django_filters.FilterSet):

    class Meta:
        model = Students
        fields = ['department','first_name','admission_number']