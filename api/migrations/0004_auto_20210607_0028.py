# Generated by Django 3.2.4 on 2021-06-07 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210606_2354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='location',
        ),
        migrations.RemoveField(
            model_name='talent',
            name='location',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='location',
        ),
        migrations.AddField(
            model_name='appuser',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='country',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='state',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='talent',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='talent',
            name='country',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='talent',
            name='state',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='country',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='state',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
