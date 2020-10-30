from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import UsersView

app_name = "users"

urlpatterns = [
    # path('signup/', views.SignUp.as_view(), name='signup'),
    path('users/', UsersView.as_view()),
    path('users/<int:pk>', UsersView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)