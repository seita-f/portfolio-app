from django.contrib import admin
from .models import Personal_Info, Skill, About_Me, Education, Job_Experience, Social_Media, UserImage
from django_summernote.admin import SummernoteModelAdmin

class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


# Register your models here.
""" Main Page """
# About_Me
admin.site.register(About_Me, BlogAdmin)

# Profile Image
admin.site.register(UserImage)

""" Resumen Page """
# Personal_Info
admin.site.register(Personal_Info)

# Work Experience
admin.site.register(Job_Experience, BlogAdmin)

# Education
admin.site.register(Education, BlogAdmin)

# Skill
admin.site.register(Skill)

# Link
admin.site.register(Social_Media)



