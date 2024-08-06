from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, search_jobs, register_user, login_view, CompanyNameList, CompanyDomainList, LocationList, DepartmentList

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', search_jobs),
    path('api/', include(router.urls)),
    path('api/register/', register_user),
    path('api/login/', login_view),
    path('api/company-names/', CompanyNameList.as_view(), name='company-name-list'),
    path('api/company-domains/', CompanyDomainList.as_view(), name='company-domain-list'),
    path('api/locations/', LocationList.as_view(), name='location-list'),
    path('api/departments/', DepartmentList.as_view(), name='department-list'),
]
