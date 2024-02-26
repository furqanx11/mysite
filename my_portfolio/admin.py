from django.contrib import admin
from .models import Project, About, Certification, Education, Skill
# Register your models here.
admin.site.register(Project)
admin.site.register(About)
admin.site.register(Certification)
admin.site.register(Education)
admin.site.register(Skill)