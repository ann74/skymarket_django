from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField


NULLABLE = {'null': True, 'blank': True}


class UserRoles:
    USER = "user"
    ADMIN = "admin"
    choices = (
        (USER, USER),
        (ADMIN, ADMIN),
    )


class User(AbstractBaseUser):

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role", "image"]

    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(verbose_name="Номер телефона", **NULLABLE)
    role = models.CharField(max_length=5, choices=UserRoles.choices, default=UserRoles.USER, verbose_name='Роль')
    image = models.ImageField(upload_to='users', verbose_name='Фото профиля', **NULLABLE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

