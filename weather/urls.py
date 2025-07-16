# -*- coding: utf-8 -*-
# @Time    : 2020/12/22 15:43
# @Author  : Mateosacco99
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about.html', views.about, name='about')
]
