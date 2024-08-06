from django.db import models

class CompanyName(models.Model):
    company_name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    founded_year = models.IntegerField()

    def __str__(self):
        return self.company_name
    
class CompanyDomain(models.Model):
    company_type = models.CharField(max_length=255)
    total_company_type = models.IntegerField()

    def __str__(self):
        return self.company_type
    
class Location(models.Model):
    location_name = models.CharField(max_length=255)

    def __str__(self):
        return self.location_name
    
class Department(models.Model):
    department_name = models.CharField(max_length=255)

    def __str__(self):
        return self.department_name