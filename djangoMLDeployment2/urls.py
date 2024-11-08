from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('sqlapp.urls')),
    path('',include('ClassifyApp.urls')),
    path('', include('myapp.urls')),
    path('', include('fraudapp.urls')),
    path('admin/', admin.site.urls),
]
