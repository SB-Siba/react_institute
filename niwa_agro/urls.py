from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    
    path("", include("users.urls.urls")),
    path("niwa_agro", include("app_common.urls.urls")),
    path("product", include("product.urls.urls")),  


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)