from django.urls import path
from thebible import views
from thebible.api_views import *
from django.conf.urls import url

app_name = "bible"

urlpatterns = [
    # 홈
    path('', views.thebible_home.as_view(), name="home"),
    # 읽기
    path('read/', views.thebible_read.as_view(), name="read"),
    path('read/search/', views.SearchReadView.as_view(), name="read_search"),
    # 좋아요 성구 api
    url('api/like/', like_verse_api.as_view(), name="like_verse_api"),
]