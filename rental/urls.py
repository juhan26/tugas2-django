from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('motor/<int:motor_id>/', views.motor_detail, name='motor_detail'),
    path('peminjaman/', views.peminjaman, name='peminjaman'),
    path('update_sudah_bayar/<int:peminjaman_id>/', views.update_sudah_bayar, name='update_sudah_bayar'),
     
]
