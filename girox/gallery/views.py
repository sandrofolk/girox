# from django.shortcuts import render
from django.views.generic import View, ListView

from braces.views import (
    AjaxResponseMixin,
    JSONResponseMixin,
    LoginRequiredMixin,
    SuperuserRequiredMixin,
)

from girox.gallery.models import Album, Photo


album_list = ListView.as_view(model=Album)


class AjaxPhotoUploadView(LoginRequiredMixin,
                          SuperuserRequiredMixin,
                          JSONResponseMixin,
                          AjaxResponseMixin,
                          View):
    """
    View for uploading photos via AJAX.
    """
    def post_ajax(self, request, *args, **kwargs):
        try:
            album = Album.objects.get(pk=kwargs.get('pk'))
        except Album.DoesNotExist:
            error_dict = {'message': 'Album not found.'}
            return self.render_json_response(error_dict, status=404)

        uploaded_file = request.FILES['file']
        Photo.objects.create(album=album, file=uploaded_file)

        response_dict = {
            'message': 'File uploaded successfully!',
        }

        return self.render_json_response(response_dict, status=200)
