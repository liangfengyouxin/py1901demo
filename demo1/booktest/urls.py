from django.conf.urls import url
from . import views

# 给应用添加app_name
app_name = 'booktest'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^list/$',views.list,name='list'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
]