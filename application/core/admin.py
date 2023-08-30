from django.contrib import admin

from .models import Job, Education, Certification

# Register your models here.
admin.site.register(Job)
admin.site.register(Education)
admin.site.register(Certification)