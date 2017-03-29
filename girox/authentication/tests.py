from django.test import TestCase

from girox.authentication.models import MyUser

_email = 'admin@admin.com'


class MyUserModelTest(TestCase):
    def setUp(self):
        self.superUser = MyUser.objects.create_superuser(
            email=_email,
            first_name='Admin',
            password='adminadmin'
        )

    def test_str(self):
        self.assertEqual(_email, str(self.superUser))
