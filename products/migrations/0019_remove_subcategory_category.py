# Generated by Django 5.0.1 on 2024-09-20 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_photo_2_options_photo_3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
    ]
