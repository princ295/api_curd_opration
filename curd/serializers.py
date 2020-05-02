
from .models import Employee
from rest_framework import serializers


class employeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = ['url', 'pk', 'empName', 'empMobile','empEmail','postion','empCode']



