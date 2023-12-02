from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CustomUser)
admin.site.register(models.job_opening)
admin.site.register(models.application)
#admin.site.register(models.UserProfile)

class CompanyAdmin(admin.ModelAdmin):
    list_filter = ['employee_size','sector']
    search_fields = ['name']
    
admin.site.register(models.Company, CompanyAdmin)