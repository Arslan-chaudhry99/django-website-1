# Generated by Django 4.0.2 on 2022-04-21 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nusmap', '0005_blog_post_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='name',
            new_name='title',
        ),
    ]