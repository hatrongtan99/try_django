from django.urls import path
from .views import product_detail_view, product_create_view, product_raw_create_view, product_list_view, product_delete_view

app_name = "persion"

urlpatterns = [
    path("", product_list_view, name="product-list"),
    path("create/", product_create_view, name="product-create"),
    path("raw-create/", product_raw_create_view, name="raw-create"),
    path("<int:id>/", product_detail_view, name="detail-product"),
    path("delete/<int:id>/", product_delete_view, name="product_delete")
]
