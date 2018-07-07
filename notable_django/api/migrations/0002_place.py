# Generated by Django 2.0.5 on 2018-06-06 20:29

from django.db import migrations, models
from django.contrib.postgres.fields import ArrayField


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                ('place_id', models.CharField(max_length=200)),
                ('name', models.TextField()),
                ('visited', models.BooleanField()),
                ('types', ArrayField(models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
