# Generated by Django 4.0.2 on 2022-04-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nusmap', '0006_rename_name_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='short_description',
            field=models.TextField(default=True, max_length=150),
        ),
    ]
