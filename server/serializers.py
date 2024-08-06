from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CompanyName, CompanyDomain, Location, Department

class CompanyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyName
        fields = '__all__'

class CompanyDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDomain
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
