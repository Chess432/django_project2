# Generated by Django 2.2 on 2019-05-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='slug',
            field=models.SlugField(default='hello-world'),
            preserve_default=False,
        ),
    ]
