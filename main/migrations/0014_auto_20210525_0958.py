# Generated by Django 3.2.2 on 2021-05-25 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210522_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='main.Category', verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='characteristics',
            field=models.ManyToManyField(blank=True, null=True, to='main.CharacteristicProduct', verbose_name='Характеристики'),
        ),
    ]