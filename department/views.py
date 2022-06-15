from django.shortcuts import get_object_or_404
from django.urls import reverse
from .forms import DepartmentForm
from django.views.generic import (
    DetailView,
    DeleteView,
    UpdateView,
    CreateView
)

from mainapp.models import Department

class Department_Create(CreateView):
    queryset = Department.objects.all()
    template_name = 'Department_form.html'
    form_class = DepartmentForm
    success_url = '/'

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

    

class Department_View(DetailView):
    queryset = Department.objects.all()
    template_name = 'departmentview.html'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Department,id=id)

class Department_delete(DeleteView):
    queryset = Department.objects.all()
    template_name ='confirm_delete.html'
    success_url = '/'
    
    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Department,id=id)
    
class Department_update(UpdateView):
    queryset = Department.objects.all()
    template_name = 'Department_form.html'
    form_class = DepartmentForm

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Department,id=id)

    def get_success_url(self):
        id = self.kwargs.get('id')
        return reverse('deptapp:departView',kwargs={'id':id})