from django.shortcuts import render
from django.http import HttpResponse
from .models import  Personal_Info, Skill, About_Me, Education, Job_Experience, Social_Media, UserImage


# Create your views here.
def about(request):
    # Text
    queryset_1 = About_Me.objects.all()
    # Image
    queryset_2 = UserImage.objects.all()

    context = {"me": queryset_1, "image": queryset_2}
    return render(request, "homepage/about.html", context)

def resume(request):
    # Personal Info
    queryset_1 = Personal_Info.objects.all()
    # job Experience
    queryset_2 = Job_Experience.objects.all()
    # Education
    queryset_3 = Education.objects.all()
    # Skills
    queryset_4 = Skill.objects.all()
    # Social Media
    queryset_5 = Social_Media.objects.all()

    context = {"personal": queryset_1, "job": queryset_2, "education": queryset_3, "skill": queryset_4,
               "social_media": queryset_5 }

    return render(request, 'homepage/resume.html', context)


