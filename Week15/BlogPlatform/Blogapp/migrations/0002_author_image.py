# Generated by Django 4.2.3 on 2023-07-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Blogapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="author_images/"),
        ),
    ]
