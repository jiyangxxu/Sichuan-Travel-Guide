# Generated by Django 4.1.5 on 2023-04-30 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sichuaninfo', '0003_alter_city_city_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bar',
            name='attraction_address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bar',
            name='attraction_website',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotel_address',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotel_website',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='localfav',
            name='attraction_address',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='localfav',
            name='attraction_website',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='mall',
            name='attraction_address',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='mall',
            name='attraction_website',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='monument',
            name='attraction_address',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='monument',
            name='attraction_website',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='museum',
            name='attraction_address',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='museum',
            name='attraction_website',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='zoo',
            name='attraction_address',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='zoo',
            name='attraction_website',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]