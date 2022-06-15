from .models import Students
import django_filters

# This studentFilter class will filter first name by first letter to last,department,add_number
# "icontain" attr help to filter first name word by word


class StudentFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Students
        fields = ['department', 'admission_number']
