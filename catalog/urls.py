from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import ProductDetailsView, HomeView, ContactsView, ProductListView
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>/', ProductDetailsView.as_view(), name='product_details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
