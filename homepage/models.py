from django.db import models
from django.forms import Textarea

# Create your models here.
""" About Me  (main page) """
class About_Me(models.Model):
    text = models.TextField()
    # text = {models.TextField: {'widget': Textarea(attrs={'height: 1em'})}}

    def __str__(self):
        return self.text


""" Profile Pic  (About Page) """
class UserImage(models.Model):
    image = models.ImageField(upload_to='images/')



""" Personal Info (Resume page) """
class Personal_Info(models.Model):
    name = models.CharField(max_length=20)
    profession = models.CharField(max_length=30)
    email_address = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


"""" Job Experience (Resume page) """
class Job_Experience(models.Model):
    year = models.CharField(max_length=20)
    role = models.CharField(max_length=40)
    company = models.CharField(max_length=40)
    text = models.TextField()

    def __str__(self):
        return self.year


"""" Education (Resume page) """
class Education(models.Model):
    school = models.CharField(max_length=30)
    year = models.CharField(max_length=20)
    text = models.TextField()

    def __str__(self):
        return self.school


"""" Skill (Resume page) """
class Skill(models.Model):
    skill_name = models.CharField(max_length=40)
    percentage = models.CharField(max_length=5)

    def __str__(self):
        return self.skill_name


""" Link (Resume Page) """
class Social_Media(models.Model):
    name_social_media = models.CharField(max_length=40)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name_social_media

