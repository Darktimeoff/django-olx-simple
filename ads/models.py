from django.db import models
from django.utils.text import slugify


class Ad(models.Model):
    class Meta:
        verbose_name_plural = 'Ads'

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Ad, self).save(*args, **kwargs)


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
