# Generated by Django 4.1.6 on 2023-07-09 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BloggingApp', '0004_blog_date_of_creation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name_plural': 'Blogs'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
