# Generated by Django 2.2.2 on 2019-06-29 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('data', models.TextField(blank=True)),
            ],
        ),
    ]
