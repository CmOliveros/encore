# Generated by Django 3.2.4 on 2021-06-07 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210607_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='venueuser',
            name='lat',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='venueuser',
            name='long',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]