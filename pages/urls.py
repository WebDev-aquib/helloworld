from django.urls import path,include
from .views import homepageview

urlpatterns = [
    
    path('', homepageview, name='home' )
]