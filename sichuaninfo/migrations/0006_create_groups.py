# create user groups

from django.db import migrations

GROUPS = [
    {
        'name': 'user',
    },
    {
        'name': 'reviewer',
    },
    {
        'name': 'updater',
    },
]


def add_group_data(apps, schema_editor):
    group_model_class = apps.get_model('auth', 'Group')
    for group in GROUPS:
        group_object = group_model_class.objects.create(
            name=group['name'],
        )


def remove_group_data(apps, schema_editor):
    group_model_class = apps.get_model('auth', 'Group')
    for group in GROUPS:
        group_object = group_model_class.objects.get(
            name=group['name']
        )
        group_object.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('sichuaninfo', '0005_cuisine_city_hotel_hotel_tel'),
    ]

    operations = [

        migrations.RunPython(
            add_group_data,
            remove_group_data
        )

    ]
