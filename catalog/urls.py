from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import product_list, product_detail, home, contacts
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
