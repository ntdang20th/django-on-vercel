"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include("demo.urls")),
    path('api/', include('api.urls')),
    path('patient/', include('patient.urls')),
    path('address/', include('address.urls')),
    path('device/', include('device.urls')),
    path('doctor/', include('doctor.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('get-token/', TokenObtainPairView.as_view(), name='get-token'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),
    path('verify-token/', TokenVerifyView.as_view(), name='verify-token'),
]

urlpatterns += staticfiles_urlpatterns()

