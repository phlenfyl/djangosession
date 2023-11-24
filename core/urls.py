
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path('',include('base.urls')),
    path('shop/',include('commerce.urls')),
    path('checkout',include('productcart.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.COMPRESS_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

