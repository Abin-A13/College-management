from .views import Department_View, Department_delete, Department_update, Department_Create
from django.urls import path

# name_space for this app
# all class import form views

app_name = "deptapp"

urlpatterns = [
    path('', Department_Create.as_view(), name="adddept"),
    path('<int:id>', Department_View.as_view(), name="departView"),
    path('<int:id>/delete/', Department_delete.as_view(), name="departdel"),
    path('<id>/update', Department_update.as_view(), name="departupdate")
]
