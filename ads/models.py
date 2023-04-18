from django.db import models
from django.utils.text import slugify
from authentication.models import User


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

class Selection(models.Model):
    class Meta:
        verbose_name_plural = 'Selections'

    name  = models.CharField(max_length=100)

    items = models.ManyToManyField(Ad, related_name='selections', default=None)

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='selections'
    )