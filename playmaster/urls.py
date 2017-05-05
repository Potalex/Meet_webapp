from django.conf.urls import url
from . import views


urlpatterns = [
  url(r'^$',views.main, name='main'),
  url(r'^act/(?P<pk>[0-9]+)$', views.act_detail, name='act_detail'),
  
]