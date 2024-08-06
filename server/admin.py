from django.contrib import admin
from .models import CompanyName, CompanyDomain, Location, Department

admin.site.register(CompanyName)
admin.site.register(CompanyDomain)
admin.site.register(Location)
admin.site.register(Department)
