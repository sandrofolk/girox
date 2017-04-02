from django.conf.urls import url

from girox.event.views import list_event, subscription_new, subscription_detail, subscription_regulation


urlpatterns = [
    url(r'^$', list_event, name='event_list'),
    url(r'^inscricao/(?P<event>\d+)/$', subscription_new, name='subscription_new'),
    url(r'^regulamento/(?P<event>\d+)/$', subscription_regulation, name='subscription_regulation'),
    url(r'^inscricao/(?P<event>\d+)/(?P<pk>\d+)/$', subscription_detail, name='subscription_detail'),
]