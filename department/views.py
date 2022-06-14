from django.shortcuts import render,get_object_or_404
from django.views.generic import (
    DetailView,
    DeleteView,
    UpdateView
)

from mainapp.models import Department,Hod

class Department_View(DetailView):
    model = Department
    template_name = 'departmentview.html'

    def get_object(self):
        id = self.kwargs.get('pk')
        return get_object_or_404(Department,id=id)

class Department_delete(DeleteView):
    model= Department
    template_name ='confirm_delete.html'
    success_url = '/'
    
    def get_object(self):
        id = self.kwargs.get('pk')
        return get_object_or_404(Department,id=id)
    
class Department_update(UpdateView):
    model = Department
    template_name = 'Departupdate_Form.html'
    success_url = '/'
    fields = ['name']
