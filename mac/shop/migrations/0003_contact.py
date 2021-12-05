# Generated by Django 3.2.5 on 2021-08-28 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210811_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
    ]
