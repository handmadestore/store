# Generated by Django 3.2.2 on 2021-05-14 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210514_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='promo_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.promocode', verbose_name='Промокод'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='sum_with_discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Сумма корзины с учетом скидки'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='sum_without_discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Сумма корзины без учета скидки'),
        ),
    ]
