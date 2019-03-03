"""games URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from blog import views
from users import views as user_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/',user_view.register, name='register'),
    url(r'^profile/',user_view.profile, name='profile'),
    url(r'^login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'^logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'^password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    url(r'^password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm'
    ),
    name='password_reset_confirm'),
    url(r'^blog/',include('blog.urls')), 
]   

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
