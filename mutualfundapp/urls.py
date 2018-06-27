from django.conf.urls import url
from . import views

app_name = 'mutualfundapp'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^register/$', views.register, name='register'),
    url(r'^r1$/', views.r1, name='r1'),
    url(r'^login/', views.login, name='login'),
]
