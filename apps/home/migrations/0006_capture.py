# Generated by Django 3.2.16 on 2023-04-25 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='capture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField(default=True)),
            ],
        ),
    ]