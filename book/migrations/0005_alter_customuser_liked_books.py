# Generated by Django 4.2.1 on 2023-09-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='liked_books',
            field=models.JSONField(default='{}'),
        ),
    ]
