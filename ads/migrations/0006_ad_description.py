# Generated by Django 4.2 on 2023-04-04 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_remove_ad_user_alter_ad_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='description',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
