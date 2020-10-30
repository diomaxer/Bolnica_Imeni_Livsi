from django.contrib import admin
from django.urls import path, include
from prod.views import all_view, home_view
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from rest_framework.routers import SimpleRouter

# router = SimpleRouter()
# router.register('api/orders', OrderView)
# router.register('api/images', ImageView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('all/', all_view, name='all'),
    path('', home_view, name='home'),
    # path('account/', include('allauth.urls')),
    # path('create/', post),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #path('users/', include('users.urls')),
    #path('users/', include('django.contrib.auth.urls')),
    # api
    path('api/', include('prod.urls')),
    path('api/', include('users.urls')),

]

# urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)