
from django.urls import path, include

from curd import views

urlpatterns = [

    path('post-req/', views.EmployeeCreateView.as_view(), name=views.EmployeeCreateView.name),
    path('employee/', views.EmployeeListView.as_view(), name=views.EmployeeListView.name),
    path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name=views.EmployeeDetailView.name),
]