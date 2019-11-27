# Generated by Django 2.2.7 on 2019-11-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=50, verbose_name='Web site')),
                ('client_name', models.CharField(max_length=50, verbose_name='Имя Клиента')),
                ('description', models.TextField(max_length=50, verbose_name='Описание')),
                ('phone', models.CharField(max_length=50, verbose_name='Контакты')),
                ('price', models.CharField(max_length=50, verbose_name='Цена')),
                ('date', models.DateField(max_length=50, verbose_name='Абонплата')),
            ],
        ),
    ]