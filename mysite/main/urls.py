from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),    
    path('home/', views.home, name='home'),  
    path('create/', views.create, name='create'),  
    path('view/', views.view, name='view'),    
    path('report/', views.report, name='report'),
    path('<int:id>', views.index, name='index'),
    path('users/', views.users, name='users'),
]



