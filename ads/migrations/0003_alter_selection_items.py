# Generated by Django 4.2 on 2023-04-18 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_selection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selection',
            name='items',
            field=models.ManyToManyField(default=None, related_name='selections', to='ads.ad'),
        ),
    ]