from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from sysfolk.authentication.models import MyUser
from sysfolk.authentication.permissions import IsAccountOwner
from sysfolk.authentication.serializers import MyUserSerializer
from django.utils.translation import ugettext as _


class MyUserViewSet(viewsets.ModelViewSet):
    lookup_field = 'email'
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            MyUser.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': _('Bad request'),
            'message': _('Account could not be created with received data.')
        }, status=status.HTTP_400_BAD_REQUEST)
