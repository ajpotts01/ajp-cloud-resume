from django.contrib import admin

from .models import Job, Education, Certification, Skill

# Register your models here.
admin.site.register(Job)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Skill)
