from django.urls import path
from . import  views
urlpatterns = [
    path('', views.home, name='FotoEditor-editPage'),
    path('editPage', views.editPage, name='FotoEditor-editPage')
]
