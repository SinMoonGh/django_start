from blog import views
from django.urls import path, re_path

app_name = 'blog'
urlpatterns = [
    path('', views.PostLV.as_view(), name='index'),
    re_path(r'^post/(?P<slug>[-\w]+)$', views.PostDV.as_view(), name = 'post_detail'),
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),
    # path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    # path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
    # path('search/', views.SearchFormView.as_view(), name='search'),
]