from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name="почта")
    phone = models.CharField(max_length=35, verbose_name="телефон", blank=True, null=True)
    avatar = models.ImageField(upload_to="users_list/avatars", verbose_name="аватар", blank=True, null=True)
    country = models.CharField(max_length=50,verbose_name="страна", blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email  # Например, используем email как username
        super().save(*args, **kwargs)