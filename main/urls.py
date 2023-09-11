"""Berkas urls.py pada aplikasi main bertanggung jawab untuk mengatur rute 
    URL yang terkait dengan aplikasi main."""

from django.urls import path #untuk mendefinisikan pola URL
from main.views import show_item #sebagai tampilan yang akan ditampilkan ketika URL terkait diakses

app_name = 'main'

urlpatterns = [
    path('', show_item, name='show_item'),
]