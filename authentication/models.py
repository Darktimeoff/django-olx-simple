from django.db import models
from django.contrib.auth.models import AbstractUser

class Location(models.Model):
    class Meta:
        verbose_name_plural = 'Locations'

    name = models.CharField(max_length=100)

    lng = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

class User(AbstractUser):
    MALE = 'm'
    FEMALE = 'f'
    SEX = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    sex = models.CharField(max_length=1, choices=SEX, default=MALE)

    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLES = [
        (MEMBER, "Пользователь"),
        (MODERATOR, "Модератор"),
        (ADMIN, "Админ"),
    ]

    role = models.CharField(max_length=10, choices=ROLES, default=MEMBER)

    age = models.PositiveIntegerField(default=0)

    locations = models.ManyToManyField(Location, default=[])

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        

    def __str__(self):
        return self.username
