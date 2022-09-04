"""Define padrões de URL para learning_logs.""" 
from django.urls import re_path
from . import views 

urlpatterns = [
         re_path(r'^$', views.index, name='index'), 
         ]

