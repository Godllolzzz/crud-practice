from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage, name="homepage"),
    path('delete/<int:id>', DeleteStudent, name="delete"),
    path('edit/<int:id>', EditStudent, name="edit"),
]
