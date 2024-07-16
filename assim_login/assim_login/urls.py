from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', accounts_views.signup_step1, name='signup'),
    path('', include('django.contrib.auth.urls')),  # For login/logout
]
