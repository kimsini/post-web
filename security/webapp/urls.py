from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^loginAction', views.loginAction, name='loginAction'),
    url(r'^login', views.login, name='login'),
    url(r'^main/page/$', views.main_page, name='main_page'),
    url(r'^history/page/$', views.history_page, name='history_page'),
    url(r'^user/info/$', views.user_info, name='user_info'),
    url(r'^RegisterDevice/$', views.RegisterDevice, name='RegisterDevice'),
    url(r'^device/(?P<pk>[0-9]+)/edit/$', views.device_edit, name='device_edit'),
    url(r'^delete/(?P<pk>[0-p]+)/device/$',views.delete_device, name='delete_device'),
    url(r'^change/(?P<pk>[0-p]+)/info/$', views.change_user, name='change_user'),
    url(r'^join/$',views.join_user, name='join_user'),
    url(r'^$', views.logout_page,name='logout_page'),
]

