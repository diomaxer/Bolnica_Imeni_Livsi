from django.contrib import admin
from django.urls import path, include
from prod.views import all_view, home_view, post
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from users.views import lk_view
from prod import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('all/', all_view, name='all'),
    path('', home_view, name='home'),

    # PRODUCT

    path('create/', post, name='create'),
    path('watch/', include('prod.urls')),

    # USER
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('lk/', lk_view, name='lk'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)