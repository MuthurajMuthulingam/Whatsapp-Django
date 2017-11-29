from django.conf.urls import url,include
from messaging import views

urlpatterns = [url(r'^messages/$',views.MessageList.as_view()),
               url(r'^messageDetails/(?P<pk>[0-9]+)/$', views.MessageDetail.as_view()),
               ]