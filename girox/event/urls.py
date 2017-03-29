from django.conf.urls import url

from girox.event.views import list, subscription_new, subscription_detail


urlpatterns = [
    url(r'^$', list, name='list'),
    url(r'^inscricao/$', subscription_new, name='subscription_new'),
    url(r'^inscricao/(?P<pk>\d+)/$', subscription_detail, name='subscription_detail'),
]