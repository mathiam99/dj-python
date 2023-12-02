from django.db import models
import uuid
from tinymce.models import HTMLField
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    size_choice = (
        ('0 - 10', '0 - 10'),
        ('10 - 30', '10 - 30'),
        ('30 - 50', '30 - 50'),
        ('50 - 100+', '50 - 100+')
    )
    employee_size = models.CharField(max_length=15, choices=size_choice)
    sector_choice =(
        ('Construction','Construction'),
        ('Financial Services','Financial Services'),
        ('Foodservice','Foodservice'),
        ('Healthcare','Healthcare'),
        ('Technology & Telecom','Technology & Telecom'),
        ('Other','Other')
    )
    sector = models.CharField(max_length=50, choices=sector_choice)
    logo = models.ImageField(upload_to="images/")
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.name} - {self.sector}"
    
    class meta:
        verbose_name_plural = "Companies"


class job_opening(models.Model):    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    position_name = models.CharField(max_length=100)
    reference = models.UUIDField(default=uuid.uuid4, editable=False)
    description = HTMLField()
    contrat_type =(
        ('permanent contract','permanent contract'),
        ('fixed-term','fixed-term'),
        ('Internship','Internship'),
    )
    type = models.CharField(max_length=50, choices=contrat_type, default=None)
    salary = models.FloatField()
    expiration_date = models.DateField()
    Company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.position_name} - {self.Company} - {self.expiration_date}'
        

    class meta:
        verbose_name_plural = "Job Openings"



class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    birth_date = models.DateField(auto_now=False, auto_now_add=False, default=None, null=True, blank=True,)
    Phone = models.CharField(max_length=15)
    

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.Phone}'
    
    class meta:
        verbose_name_plural = "Users"


class application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    job_opening = models.ForeignKey(job_opening, on_delete=models.SET_NULL, null=True, blank=True)
    attachement = models.FileField(upload_to="pdfs/")

    def __str__(self):
        return f'{self.user} - {self.job_opening}, {self.attachement}'

    class meta:
        verbose_name_plural = "Applications"



'''class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username'''