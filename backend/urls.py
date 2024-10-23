from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from users.views import TaskView
from news.views import NewsListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),

    path('api/tasks/', TaskView.as_view()),

    path('api/news/', NewsListView.as_view()),
	
    path('api/check-lists/', include('check_lists.urls')), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
