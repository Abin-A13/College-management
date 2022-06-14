from mainapp import views
from .views import Student_view,Student_delete,Student_update
from django.urls import path

app_name = "studapp"

urlpatterns = [
    path('', views.home, name="home"),
    path('addstudents/', views.addstudents, name="addstd"),

    # class based views
    path('studentsview/<int:id>', Student_view.as_view(), name="stdview"),
    path('<int:pk>/delete', Student_delete.as_view(), name="stddel"),
    path('<int:pk>/update', Student_update.as_view(), name="stdupdate"),
]