from django.conf.urls import url,include
import messaging
from rest_framework.authtoken import views

urlpatterns = [url(r'^messages/$',messaging.views.MessageList.as_view()),
               url(r'^messageDetails/(?P<pk>[0-9]+)/$', messaging.views.MessageDetail.as_view()),
               url(r'^users/$', messaging.views.Users.as_view()),
               url(r'^user/(?P<pk>[0-9]+)/$', messaging.views.UserDetails.as_view()),
               url(r'^groups/$', messaging.views.GroupList.as_view()),
               ]
# #Login
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]

#Authontication
urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token)
]