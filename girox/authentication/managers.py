from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, password, **extra_fields):
        """
        Creates and saves a User with the given email, first_name and password.
        """
        if not email:
            raise ValueError(_('Users must have an email address'))
        if not first_name:
            raise ValueError(_('Users must have an first name'))
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, first_name and password.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, password, **extra_fields)

    def create_superuser(self, email, first_name, password, **extra_fields):
        """
        Creates and saves a superuser with the given email, first_name and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self._create_user(email, first_name, password, **extra_fields)

        # user = self.create_user(
        #     email,
        #     first_name=first_name,
        #     password=password,
        # )
        # user.is_staff = True
        # user.is_admin = True
        # user.save(using=self._db)
        # return user
