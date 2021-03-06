# Generated by Django 3.2.10 on 2021-12-10 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(default=0)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.cart')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer')),
            ],
        ),
    ]
