# Generated by Django 4.1.5 on 2023-05-03 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sichuaninfo', '0007_create_group_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_tel',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
