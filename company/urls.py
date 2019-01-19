from django.contrib import admin
from django.urls import path

from app01 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('teacher/', views.teacher),


    path('slider/', views.slider),

]
