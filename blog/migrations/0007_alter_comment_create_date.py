# Generated by Django 4.1 on 2024-08-19 10:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comment_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 19, 10, 16, 3, 666326, tzinfo=datetime.timezone.utc)),
        ),
    ]
