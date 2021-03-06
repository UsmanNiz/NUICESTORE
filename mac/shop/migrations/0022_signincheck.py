# Generated by Django 3.2.10 on 2021-12-13 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_delete_signincheck'),
    ]

    operations = [
        migrations.CreateModel(
            name='signincheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField(default=1)),
                ('sign', models.BooleanField(default=False)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer')),
            ],
        ),
    ]
