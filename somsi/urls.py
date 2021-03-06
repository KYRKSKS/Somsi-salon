"""SomSiSalon URL Configuration
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
from functools import cached_property
from django.contrib import admin
from django.urls import path

from index import views as index_views
from aboutus import views as aboutus_views
from appointment import views as appointment_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_views.index, name='index'),
    path('aboutus',aboutus_views.index,name="aboutus"),
    path('aboutus_list',index_views.AboutUsList.as_view(),name='AboutUsList'),
    path('aboutus_detail',index_views.AppointmentDetail.as_view(),name='AppointmentDetail'),

    path('appointment', appointment_views.index, name='appointment'),
    path('appointment_list',index_views.AppointmentList.as_view(),name='AppointmentList'),
    path('appointment_detail',index_views.AppointmentDetail.as_view(),name='AppointmentDetail'),
    

    path('best_product_seller', index_views.BestProductSeller.as_view(),
         name='BestProductSeller'),
    path('best_service_seller', index_views.BestServiceSeller.as_view(),
         name='BestServiceSeller'),

    path('mail_register_for_infomation', index_views.MailRegister.as_view(),
         name='MailRegisterForInfomation'),
]