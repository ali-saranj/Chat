# Generated by Django 4.1.4 on 2022-12-11 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameSender', models.CharField(max_length=10000)),
                ('sms', models.CharField(max_length=10000)),
            ],
        ),
    ]