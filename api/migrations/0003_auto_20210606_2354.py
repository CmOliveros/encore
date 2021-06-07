# Generated by Django 3.2.4 on 2021-06-06 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_appuser_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.JSONField(default=dict)),
                ('members', models.JSONField(default=list)),
                ('discography', models.JSONField(default=list)),
                ('events', models.JSONField(default=list)),
                ('fans', models.JSONField(default=list)),
                ('genres', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.JSONField(default=dict)),
                ('events', models.JSONField(default=list)),
                ('fans', models.JSONField(default=list)),
            ],
        ),
        migrations.AddField(
            model_name='appuser',
            name='friends',
            field=models.JSONField(default=list),
        ),
    ]