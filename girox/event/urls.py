from django.conf.urls import url

from girox.event.views import list_event, subscription_new, subscription_detail, subscription_regulation, event_detail


urlpatterns = [
    url(r'^$', list_event, name='event_list'),
    url(r'^(?P<pk>\d+)/', event_detail, name='event_detail'),
    url(r'^inscricao/(?P<event>\d+)/$', subscription_new, name='subscription_new'),
    url(r'^inscricao/(?P<event>\d+)/(?P<pk>\d+)/$', subscription_detail, name='subscription_detail'),
    url(r'^regulamento/(?P<event>\d+)/$', subscription_regulation, name='subscription_regulation'),
]
