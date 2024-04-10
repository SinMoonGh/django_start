# photo/urls.py
from django.urls import path
from . import views

app_name = 'photo'  # URL 네임스페이스 설정
urlpatterns = [
    path('albums/<int:album_id>/', views.album_detail, name='album_detail'),
]