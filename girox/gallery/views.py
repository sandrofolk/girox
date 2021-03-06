from django.views.generic import View, DetailView

from braces.views import (
    AjaxResponseMixin,
    JSONResponseMixin,
    LoginRequiredMixin,
    # SuperuserRequiredMixin,
    StaffuserRequiredMixin,
    PermissionRequiredMixin,
)

from girox.advertising.mixins import ListViewAdvertiser, DetailViewAdvertiser
from girox.gallery.models import Album, Photo


album_list = ListViewAdvertiser.as_view(model=Album)

album_detail = DetailViewAdvertiser.as_view(model=Album)

# album_detail_test = DetailView.as_view(model=Album, template_name="gallery/album_detail_test.html")

photo_detail = DetailView.as_view(model=Photo)


class AjaxPhotoUploadView(LoginRequiredMixin,
                          StaffuserRequiredMixin,
                          PermissionRequiredMixin,
                          JSONResponseMixin,
                          AjaxResponseMixin,
                          View):
    """
    View for uploading photos via AJAX.
    """
    permission_required = "gallery.add_photo"

    def post_ajax(self, request, *args, **kwargs):
        try:
            album = Album.objects.get(pk=kwargs.get('pk'))
        except Album.DoesNotExist:
            error_dict = {'message': 'Album não encontrado.'}
            return self.render_json_response(error_dict, status=404)

        uploaded_file = request.FILES['file']
        Photo.objects.create(album=album, file=uploaded_file)

        response_dict = {
            'message': 'Arquivo enviado com sucesso!',
        }

        return self.render_json_response(response_dict, status=200)
