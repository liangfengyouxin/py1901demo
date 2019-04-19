from django.conf.urls import url
from . import views

# 给应用添加app_name
app_name = 'booktest'

urlpatterns = [
    # 通过url函数设置url路由配置项
    # 在应用的urls文件中进行url配置的时候：
    # 1、严格匹配开头和结尾（$）
    url(r'^index/$',views.index,name='index'),    #建立/index和视图index之间的关系
    url(r'^list/$',views.list,name='list'),     #显示图书信息
    #显示英雄信息,(\d+)为组,django在调用视图函数时,组的内容为参数,可传入到对应的视图函数中去
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^delete/(\d+)/$',views.delete,name='delete'),
    url(r'^addhero/(\d+)/$',views.addhero,name='addhero'),
    url(r'^addherohandler/$',views.addherohandler,name='addherohandler')
]