from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name="show"),
    path('create', views.stud, name="stud"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.destroy, name="delete")
]