# Generated by Django 5.0.7 on 2024-10-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0016_alter_bookpicture_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookpicture',
            name='picture',
            field=models.ImageField(upload_to='book_covers/'),
        ),
    ]
