# Generated by Django 5.0.2 on 2024-02-17 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_articles_photo_alter_articles_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='published',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 2, 17, 20, 0, 51, 698267, tzinfo=datetime.timezone.utc)),
        ),
    ]
