from unicodedata import name
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('filter/', views.filter_data, name='filter_data'),
    path('data/<str:pk>/', views.show_data, name='data'),
]