# Generated by Django 5.0.7 on 2024-10-29 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0024_rating_feedback_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]