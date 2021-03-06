# Generated by Django 3.2.2 on 2021-05-14 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210514_1145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'verbose_name_plural': 'Корзины'},
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_without_discount', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Стоимость без учета скидки')),
                ('cost_with_discount', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Стоимость с учетом скидки')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('final_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Общая стоимость')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name_plural': 'Товары в заказе',
            },
        ),
    ]
