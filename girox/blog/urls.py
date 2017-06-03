from django.conf.urls import url

from girox.blog.views import post_list, post_detail


urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^post/(?P<slug>[^\.]+)', post_detail, name='post_detail'),
]
