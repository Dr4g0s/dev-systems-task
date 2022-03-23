from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, phone_number, password, is_staff, is_superuser, **extra_fields):
        user = self.model(phone_number=phone_number,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          date_joined=timezone.now(), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, phone_number, password, **extra_fields):
        return self._create_user(phone_number, password, False, False, **extra_fields)

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields['birthdate'] = (timezone.now() - timezone.timedelta(days=365)).date()
        return self._create_user(phone_number, password, True, True, **extra_fields)
