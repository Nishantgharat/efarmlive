# Generated by Django 3.1.7 on 2021-05-04 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20210503_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='donateme',
            name='created_on',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='donateme',
            name='debt',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='donateme',
            name='descp',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donateme',
            name='fund_req',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='donateme',
            name='monthly_exp',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='donateme',
            name='monthly_inc',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='donateme',
            name='title',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
