from django.contrib import admin

# Register your models here.
from .models import Ad,Applicant

admin.site.register(Ad)
admin.site.register(Applicant)