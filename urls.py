
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns =[
    path('hello/',include('hello.urls')),
    path('admin/',admin.site.urls),
    path('atelier/', include('atelier.urls')),
    path('magasin/', include('magasin.urls')),

   
]
