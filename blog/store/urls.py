from django.urls import path
from . import views

urlpatterns = [
#Leave as empty string for base url

path('', views.home, name="home"),
path('pets/', views.pets, name="pets"),
path('feature/', views.feature, name="feature"),
path('contact/', views.contact, name="contact"),
path('nature/', views.nature, name="nature"),
path('community/', views.community, name="community"),

]

