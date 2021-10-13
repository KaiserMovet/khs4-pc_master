# Generated by Django 3.2.7 on 2021-10-12 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('mac', models.CharField(max_length=18, primary_key=True, serialize=False, unique=True)),
                ('port', models.IntegerField()),
                ('ip', models.CharField(max_length=18)),
                ('last_seen', models.DateTimeField()),
            ],
        ),
    ]
