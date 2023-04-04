from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify


class Location(models.Model):
    class Meta:
        verbose_name_plural = 'Locations'

    name = models.CharField(max_length=100)

    lng = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name


class User(models.Model):
    ROLE = [
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
        ('member', 'Member'),
    ]

    class Meta:
        verbose_name_plural = 'Users'

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=100)

    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])

    role = models.CharField(max_length=10, choices=ROLE, default='member')

    location = models.ForeignKey(
        Location, null=True, on_delete=models.SET_NULL, related_name='users')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)


class Ad(models.Model):
    class Meta:
        verbose_name_plural = 'Ads'

    image = models.ImageField(upload_to='ads/', blank=True, null=True)

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    slug = models.SlugField(max_length=100, unique=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    is_published = models.BooleanField(default=False)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ads')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='ads')

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Ad, self).save(*args, **kwargs)
