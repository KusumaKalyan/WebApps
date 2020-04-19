from django.urls import path
from . import  views
urlpatterns = [
    path('', views.home, name='FotoEditor-home'),
    path('editPage', views.editPage, name='FotoEditor-editPage')
]
