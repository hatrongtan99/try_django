
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("products/", include("persion.urls")),
    path("article/", include("article.urls"))
]
