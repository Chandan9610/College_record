from django.contrib import admin
from django.urls import path
from studentauth import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('add_record/', views.add_record, name='add_record'),
    path('record/<int:pk>', views.student_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('update_record/', views.update_record, name='update_record'),





    
]