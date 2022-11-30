from django.contrib import admin
from django.urls import path, include
from core.views import mainpage
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('store.urls')),
    path('', mainpage, name='mainpage'),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
