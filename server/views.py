from django.http import JsonResponse
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer, CompanyNameSerializer, CompanyDomainSerializer, LocationSerializer, DepartmentSerializer
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from .models import CompanyName, CompanyDomain, Location, Department

class CompanyNameList(generics.ListAPIView):
    queryset = CompanyName.objects.all()
    serializer_class = CompanyNameSerializer

class CompanyDomainList(generics.ListAPIView):
    queryset = CompanyDomain.objects.all()
    serializer_class = CompanyDomainSerializer

class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class DepartmentList(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        return JsonResponse({'user_id': user.id}, status=200)
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=400)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def search_jobs(request):
    api_url = "https://findwork.dev/api/jobs/"
    api_key = "855c442e027143b104c71dfd01a65ab9b3cb3f2b"
    
    headers = {
        'Authorization': f'Token {api_key}',
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        jobs = response.json().get('results', [])
        data = {'jobs': jobs}
    else:
        data = {'error': f'Failed to fetch jobs, status code: {response.status_code}'}

    return JsonResponse(data)

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username and password:
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
