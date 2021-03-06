# Generated by Django 3.2.2 on 2021-05-13 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('surname', models.CharField(blank=True, max_length=50, verbose_name='Фамилия')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Номер телефона')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование категории')),
            ],
        ),
        migrations.CreateModel(
            name='CharacteristicProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Значение')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Наименование товара')),
                ('description', models.CharField(max_length=500, verbose_name='Описание товара')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Стоимость за ед.')),
                ('category', models.ManyToManyField(to='main.Category')),
                ('characteristics', models.ManyToManyField(to='main.CharacteristicProduct')),
            ],
        ),
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Сумма применения')),
                ('discount', models.IntegerField(verbose_name='Скидка в руб.')),
                ('date_beginning', models.DateTimeField(verbose_name='Дата начала действия скидки')),
                ('date_expiration', models.DateTimeField(verbose_name='Дата окончания действия скидки')),
                ('is_active', models.BooleanField(default=False, verbose_name='Актуальность промокода')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Описание промокода')),
            ],
        ),
        migrations.CreateModel(
            name='TypeCharacteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование типа')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum_without_discount', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Сумма корзины без учета скидки')),
                ('sum_with_discount', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Сумма корзины с учетом скидки')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания корзины')),
                ('is_added_in_order', models.BooleanField(default=False, verbose_name='Корзина добавлена в заказ?')),
                ('promo_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.promocode', verbose_name='Промокод')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_without_discount', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Стоимость без учета скидки')),
                ('cost_with_discount', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Стоимость с учетом скидки')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('final_cost', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Общая стоимость')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='Товар')),
                ('shopping_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.shoppingcart', verbose_name='Корзина')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=350, verbose_name='Адрес')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')),
                ('date_delivery', models.DateTimeField(auto_now_add=True, verbose_name='Дата доставки')),
                ('shopping_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.shoppingcart', verbose_name='Корзина')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Название изображения')),
                ('is_main', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
        migrations.AddField(
            model_name='characteristicproduct',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.typecharacteristic'),
        ),
    ]
