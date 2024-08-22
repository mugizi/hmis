from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.login, name='login'),
     path('logout', views.custom_logout_view, name='logout'),
    path('adduser/', views.adduser, name='adduser'),
     path('viewusers/', views.viewusers, name='viewusers'),
]