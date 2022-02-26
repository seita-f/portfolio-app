from django.conf.urls import url
from homepage import views
from django.urls import path


# TEMPLATE TAGGING
app_name = "homepage"
urlpatterns = [
    url(r'^$', views.about, name='about'),
    url(r'^resume/$', views.resume, name='resume'),
]


