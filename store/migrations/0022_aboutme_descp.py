# Generated by Django 3.1.7 on 2021-05-09 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_auto_20210509_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='descp',
            field=models.TextField(blank=True, null=True),
        ),
    ]
