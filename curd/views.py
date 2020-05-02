from django.shortcuts import render


from rest_framework.response import Response
from rest_framework import generics
from rest_framework.reverse import reverse

from .models import Employee
from .serializers import employeeSerializer

# Create your views here.

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    
    def get(self, request):
        return Response({
            'postreq': reverse(EmployeeCreateView.name, request=request),
            'employers': reverse(EmployerListView.name, request=request),
        })


class EmployeeCreateView(generics.CreateAPIView):
    
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer
    name = 'employee-create'
    # authentication_classes


class EmployeeListView(generics.ListAPIView):
    
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer
    name = 'employee-list'
    # authentication_classes



class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer
    name = 'employee-detail'
    # authentication_classes

