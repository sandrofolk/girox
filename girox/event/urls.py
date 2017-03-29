from django.conf.urls import url

from girox.event.views import list, subscription_new, subscription_detail


urlpatterns = [
    url(r'^$', list, name='list'),
    url(r'^inscricao/(?P<event>\d+)/$', subscription_new, name='subscription_new'),
    url(r'^inscricao/(?P<event>\d+)/(?P<pk>\d+)/$', subscription_detail, name='subscription_detail'),
]