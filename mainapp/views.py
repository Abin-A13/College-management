from django.urls import reverse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import  messages
from .models import Students,Department
from django.views.generic import (
    DetailView,
    DeleteView,
    UpdateView
)
from .forms import StudentForm
from .filters import StudentFilter
#  this function is for display all department and 
def home(request):
    dep = Department.objects.all()
    std = Students.objects.all()
    myfilter = StudentFilter(request.GET,queryset=std)
    std = myfilter.qs
    context = {'department' : dep,'students' :std,'filter':myfilter}
    return render(request,'home.html',context)


def addstudents(request):
    dep = Department.objects.all()
    context = {'department' : dep }
    if request.method == 'POST':
        first_name = request.POST['firstName']
        middle_name = request.POST['Middlename']
        last_name = request.POST['lastName']
        parent = request.POST['gardian']
        Address = request.POST['addr']
        Number = request.POST['num']
        department = request.POST.get('department')
        dob = request.POST['dob']
        gender = request.POST.get('gender')
        if dob == "":
            messages.info(request, "Date of birth must provide")
            return redirect('addstd')
        adminId= first_name[0:2] + dob[-3:]
        print(adminId)
        print(gender)
        dep_obj = Department.objects.get(name=department)
        data = Students.objects.create(
            first_name=first_name,middle_name=middle_name,
            last_name=last_name,parent_name=parent,address=Address,
            number=Number,department=dep_obj,DOB=dob,gender=gender,admission_number =adminId
            )
        data.save()
        return redirect("/")

    return render(request,'register.html',context)

class Student_view(DetailView):
    queryset = Students.objects.all()
    template_name = 'students_detail.html'
    
    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Students,id=id)

class Student_delete(DeleteView):
    queryset = Students.objects.all()
    template_name ='confirm_delete.html'
    
    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Students,id=id)

    def get_success_url(self):
        return reverse('studapp:home')


class Student_update(UpdateView):
    queryset = Students.objects.all()
    template_name = 'students_form.html'
    form_class   =  StudentForm

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Students,id=id)
    
    def get_success_url(self):
        id = self.kwargs.get('id')
        return reverse('studapp:stdview',kwargs={'id':id})

    