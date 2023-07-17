from django.urls import path, re_path, include

from . import views

app_name = 'productapp'
urlpatterns = [
    path(
        'get_products_from_csv/',
        views.get_products_from_csv,
        name='get_products_from_csv'
    ),
    path(
        'get_products_images_from_csv/',
        views.get_products_images_from_csv,
        name='get_products_images_from_csv'
    ),
    # path(
    #     'product_list/',
    #     views.ProductListView.as_view(),
    #     name='product_list'
    # ),
    path(
        'product_list/',
        views.ProductListView,
        name='product_list'
    ),
    path(
        '<slug:slug>/',
        views.ProductDetailView.as_view(),
        name='product_detail'
    ),
    #path(
    #    '',
    #    views.ProductHomeView,
    #    name='product_home'
    #),
]