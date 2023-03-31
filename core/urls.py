from django.urls import path, include
from . import views





urlpatterns = [
    path('', views.home, name="home"),
    path('service/<slug:slug>/', views.service, name='service'),
    path('project/<slug:slug>/', views.project, name='project'),
    path("contact",views.contact ,name="contact")


]

