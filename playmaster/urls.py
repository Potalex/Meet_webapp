from django.conf.urls import url
from . import views


urlpatterns = [
  url(r'^$',views.main, name='main'),
  url(r'^act/(?P<pk>[0-9]+)$', views.act_detail, name='act_detail'),
  url(r'^act/new/$', views.act_new, name='act_new'),
]