from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('penulis/', views.PenulisListView.as_view(), name='penulis'),
    path('penulis/tambah/', views.PenulisCreateView.as_view(), name='tambah_penulis'),
    path('penulis/<int:pk>/', views.PenulisDetailView.as_view(), name='detail_penulis'),
    path('penulis/<int:pk>/buku/edit', views.PenulisBukuUpdateView.as_view(), name='update_buku_penulis'),
]
