from .views import Department_View,Department_delete,Department_update
from django.urls import path

app_name = "deptapp"
urlpatterns = [
 path('<int:pk>',Department_View.as_view(), name="departView" ),
 path('<int:pk>/delete',Department_delete.as_view(), name="departdel" ),
 path('<int:pk>/update',Department_update.as_view(), name="departupdate" )
]