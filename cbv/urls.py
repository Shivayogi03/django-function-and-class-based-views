"""
URL configuration for cbv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from app.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_by_fbv/',insert_by_fbv,name='insert_by_fbv'),

    path('insert_by_cbv/',insert_by_cbv.as_view(),name='insert_by_cbv'),

    path('Direct/',TemplateView.as_view(template_name='Direct.html')),
    path('RenderHTMLbyTV/',RenderHTMLbyTV.as_view(),name='RenderHTMLbyTV'),
    path('insert_by_TV/',insert_by_TV.as_view(),name='insert_by_TV'),
    path('Insertbyfv/',Insertbyfv.as_view(),name='Insertbyfv'),
]
