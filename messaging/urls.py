from django.conf.urls import url,include
from messaging import views

urlpatterns = [url(r'^messages/$',views.MessageList.as_view()),
               url(r'^messageDetails/(?P<pk>[0-9]+)/$', views.MessageDetail.as_view()),
               url(r'^users/$', views.Users.as_view()),
               url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetails.as_view()),
               ]
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]