# Generated by Django 4.0 on 2021-12-11 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_delete_signin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='cart_id',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='customer_id',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
    ]