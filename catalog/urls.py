from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import ProductDetailsView, HomeView, ContactsView, ProductListView, ProductDeleteView, \
    ProductUpdateView, ProductCreateView, ProductByCategoryView
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailsView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:category_id>/', ProductByCategoryView.as_view(), name='category_products'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
