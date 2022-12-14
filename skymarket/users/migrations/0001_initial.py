# Generated by Django 3.2.6 on 2022-11-11 08:41

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(help_text='Введите имя.', max_length=50, verbose_name='Имя.')),
                ('last_name', models.CharField(help_text='Введите фамилию.', max_length=100, verbose_name='Фамилия.')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(help_text='Введите номер телефона.', max_length=20, region=None, verbose_name='Телефон.')),
                ('email', models.EmailField(help_text='Не более 150 символов, только буквы, цифры и @/./+/-/_ @/./+/-/_.', max_length=254, unique=True, verbose_name='Логин.')),
                ('role', models.CharField(choices=[('user', 'User'), ('admin', 'Admin')], default='user', max_length=12, verbose_name='Роль.')),
                ('image', models.ImageField(null=True, upload_to='media/', verbose_name='Аватарка.')),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Пользователь.',
                'verbose_name_plural': 'Пользователи.',
            },
        ),
    ]
