from django.conf.urls import url

from girox.gallery import views


urlpatterns = [
    url(r'^$', views.album_list, name='album_list'),
    url(r'^(?P<pk>\d+)/$', views.album_detail, name='album_detail'),
    url(r'^(?P<pk>\d+)/ajax-upload/$',
        views.AjaxPhotoUploadView.as_view(),
        name='ajax_photo_upload_view',
    ),
]
