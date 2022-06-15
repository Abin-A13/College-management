from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Students, Department
from django.views.generic import (
    DetailView,
    DeleteView,
    UpdateView
)
from .forms import StudentForm
from .filters import StudentFilter

# This function is for display all department and Students
# here am using django_filter to make students data filter by words


def home(request):
    dep = Department.objects.all()
    std = Students.objects.all()
    myfilter = StudentFilter(request.GET, queryset=std)
    std = myfilter.qs
    context = {'department': dep, 'students': std, 'filter': myfilter}
    return render(request, 'home.html', context)

# To create Student detail, addstudents will do the task by check post or get method is
# here I'm use django messages method to notify on top for required field
# Admission id is create by first_name[2],"god" first 2 words "go" and date of birth  string "2022-03-14" the Day[14]


def addstudents(request):
    dep = Department.objects.all()
    context = {'department': dep}
    if request.method == 'POST':
        first_name = request.POST['firstName']
        middle_name = request.POST['Middlename']
        last_name = request.POST['lastName']
        parent = request.POST['gardian']
        Address = request.POST['addr']
        Number = request.POST['num']
        department = request.POST.get('department')
        dob = request.POST['dob']
        gender = request.POST['gender']
        if first_name == "":
            messages.info(request, "First Name must provide")
            return redirect('studapp:addstd')
        if dob == "":
            messages.info(request, "Date of birth must provide")
            return redirect('studapp:addstd')
        adminId = first_name[0:2] + dob[-3:]
        print(gender)
        dep_obj = Department.objects.get(name=department)
        data = Students.objects.create(
            first_name=first_name, middle_name=middle_name,
            last_name=last_name, parent_name=parent, address=Address,
            number=Number, department=dep_obj, DOB=dob, gender=gender, admission_number=adminId
        )
        data.save()
        return redirect("/")

    return render(request, 'register.html', context)

# here i'm using generic view like to listview,detialview to render the template and get,post,delete
# override the method get_object get the data by Id
# override the method get_success_url to redirect url_parttern names after all done


class Student_view(DetailView):
    queryset = Students.objects.all()
    template_name = 'students_detail.html'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Students, id=id)


class Student_delete(DeleteView):
    queryset = Students.objects.all()
    template_name = 'confirm_delete.html'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Students, id=id)

    def get_success_url(self):
        return reverse('studapp:home')

#  in this  class i use django forms_vaild method to get form and update


class Student_update(UpdateView):
    queryset = Students.objects.all()
    template_name = 'students_form.html'
    form_class = StudentForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Students, id=id)

    def get_success_url(self):
        id = self.kwargs.get('id')
        return reverse('studapp:stdview', kwargs={'id': id})
