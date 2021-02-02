from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.shortcuts import redirect

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 어드민
    path('admin/', admin.site.urls),
    # 그냥 홈
    path('', lambda request: redirect('thebible/read/', permanent=True)),
    # 블로그 관련
    path('blog/', include('myblog.urls')),
    # 성경관련
    path('thebible/', include('thebible.urls')),
    # 유저페이지
    path('users/', include('users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)