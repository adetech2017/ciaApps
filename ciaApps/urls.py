from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header  =  "LASG-CIA Voucher App"  
admin.site.site_title  =  "LASG-CIA"
admin.site.index_title  =  "LASG-CIA"