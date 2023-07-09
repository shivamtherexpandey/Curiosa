# Generated by Django 4.1.6 on 2023-07-09 08:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BloggingApp', '0003_rename_content_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date_of_creation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]