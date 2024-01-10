
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('accounts/', include('accounts.urls')),
    path('info/', include('apps.customer_profile.urls')),
    path('forms/', include('apps.forms.urls')),
    path('store/', include('apps.store.urls')),
    path('blog/', include('apps.blog.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)