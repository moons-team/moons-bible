from django.urls import path
from thebible import views
from thebible.api_views import *
from django.conf.urls import url

app_name = "bible"

urlpatterns = [
    path('', views.thebible_home.as_view(), name="home"), # 홈
    path('read/', views.thebible_read.as_view(), name="read"), # 읽기
    path('read/search/', views.SearchReadView.as_view(), name="read_search"), # 검색
    url('api/like/', like_verse_api.as_view(), name="like_verse_api"), # 좋아요 성구 api

    url('test/', views.test)
]