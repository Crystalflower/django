from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('<int:pk>/', products, name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
