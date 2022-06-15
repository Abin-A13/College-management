from mainapp import views
from .views import Student_view, Student_delete, Student_update
from django.urls import path

# namespace for this app
app_name = "studapp"

urlpatterns = [
    # function based views
    path('', views.home, name="home"),
    path('addstudents/', views.addstudents, name="addstd"),

    # class based views
    path('<int:id>', Student_view.as_view(), name="stdview"),
    path('<int:id>/delete/', Student_delete.as_view(), name="stddel"),
    path('<int:id>/update/', Student_update.as_view(), name="stdupd"),
]
