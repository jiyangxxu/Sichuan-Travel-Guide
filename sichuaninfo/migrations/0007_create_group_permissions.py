from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    perm_view_bar = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                           content_type__model='bar',
                                                           codename='view_bar')

    perm_add_bar = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                           content_type__model='bar',
                                                           codename='add_bar')

    perm_change_bar = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                           content_type__model='bar',
                                                           codename='change_bar')

    perm_delete_bar = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                           content_type__model='bar',
                                                           codename='delete_bar')

    perm_view_city = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                        content_type__model='city',
                                                        codename='view_city')

    perm_view_cuisine = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                               content_type__model='cuisine',
                                                               codename='view_cuisine')

    perm_add_cuisine = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                   content_type__model='cuisine',
                                                   codename='add_cuisine')

    perm_change_cuisine = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                      content_type__model='cuisine',
                                                      codename='change_cuisine')

    perm_delete_cuisine = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                      content_type__model='cuisine',
                                                      codename='delete_cuisine')

    perm_view_hotel = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                               content_type__model='hotel',
                                                               codename='view_hotel')

    perm_add_hotel = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                   content_type__model='hotel',
                                                   codename='add_hotel')

    perm_change_hotel = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                      content_type__model='hotel',
                                                      codename='change_hotel')

    perm_delete_hotel = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                      content_type__model='hotel',
                                                      codename='delete_hotel')

    perm_view_localfav = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                         content_type__model='localfav',
                                                         codename='view_localfav')

    perm_add_localfav = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                   content_type__model='localfav',
                                                   codename='add_localfav')

    perm_change_localfav = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                      content_type__model='localfav',
                                                      codename='change_localfav')

    perm_delete_localfav = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                      content_type__model='localfav',
                                                      codename='delete_localfav')

    perm_view_mall = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                       content_type__model='mall',
                                                       codename='view_mall')

    perm_add_mall = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                   content_type__model='mall',
                                                   codename='add_mall')

    perm_change_mall = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                      content_type__model='mall',
                                                      codename='change_mall')

    perm_delete_mall = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                      content_type__model='mall',
                                                      codename='delete_mall')

    perm_view_monument = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                        content_type__model='monument',
                                                        codename='view_monument')

    perm_add_monument = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                   content_type__model='monument',
                                                   codename='add_monument')

    perm_change_monument = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                      content_type__model='monument',
                                                      codename='change_monument')

    perm_delete_monument = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                      content_type__model='monument',
                                                      codename='delete_monument')

    perm_view_museum = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                             content_type__model='museum',
                                                             codename='view_museum')

    perm_add_museum = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                   content_type__model='museum',
                                                   codename='add_museum')

    perm_change_museum = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                      content_type__model='museum',
                                                      codename='change_museum')

    perm_delete_museum = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                      content_type__model='museum',
                                                      codename='delete_museum')

    perm_view_restaurant = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                             content_type__model='restaurant',
                                                             codename='view_restaurant')

    perm_add_restaurant = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                   content_type__model='restaurant',
                                                   codename='add_restaurant')

    perm_change_restaurant = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                      content_type__model='restaurant',
                                                      codename='change_restaurant')

    perm_delete_restaurant = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                      content_type__model='restaurant',
                                                      codename='delete_restaurant')

    perm_view_route = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                             content_type__model='route',
                                                             codename='view_route')

    perm_add_route = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                   content_type__model='route',
                                                   codename='add_route')

    perm_change_route = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                      content_type__model='route',
                                                      codename='change_route')

    perm_delete_route = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                      content_type__model='route',
                                                      codename='delete_route')

    perm_view_zoo = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                             content_type__model='zoo',
                                                             codename='view_zoo')

    perm_add_zoo = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                   content_type__model='zoo',
                                                   codename='add_zoo')

    perm_change_zoo = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                      content_type__model='zoo',
                                                      codename='change_zoo')

    perm_delete_zoo = permission_class.objects.filter(content_type__app_label='sichuaninfo',
                                                      content_type__model='zoo',
                                                      codename='delete_zoo')

    user_permissions = chain(perm_view_bar,
                             perm_view_mall,
                             perm_view_museum,
                             perm_view_monument,
                             perm_view_localfav,
                             perm_view_zoo,
                             perm_view_hotel,
                             perm_view_cuisine,
                             perm_view_restaurant,
                             perm_view_route,
                             perm_view_city)

    reviewer_permissions = chain(perm_view_bar,
                                 perm_change_bar,
                                 perm_delete_bar,
                                 perm_view_mall,
                                 perm_change_mall,
                                 perm_delete_mall,
                                 perm_view_museum,
                                 perm_change_museum,
                                 perm_delete_museum,
                                 perm_view_monument,
                                 perm_change_monument,
                                 perm_delete_monument,
                                 perm_view_localfav,
                                 perm_change_localfav,
                                 perm_delete_localfav,
                                 perm_view_zoo,
                                 perm_change_zoo,
                                 perm_delete_zoo,
                                 perm_view_hotel,
                                 perm_change_hotel,
                                 perm_delete_hotel,
                                 perm_view_cuisine,
                                 perm_change_cuisine,
                                 perm_delete_cuisine,
                                 perm_view_restaurant,
                                 perm_change_restaurant,
                                 perm_delete_restaurant,
                                 perm_view_route,
                                 perm_change_route,
                                 perm_delete_route,
                                 perm_view_city,
                                 )

    updater_permissions = chain(perm_view_bar,
                                 perm_change_bar,
                                 perm_add_bar,
                                 perm_view_mall,
                                 perm_change_mall,
                                 perm_add_mall,
                                 perm_view_museum,
                                 perm_change_museum,
                                 perm_add_museum,
                                 perm_view_monument,
                                 perm_change_monument,
                                 perm_add_monument,
                                 perm_view_localfav,
                                 perm_change_localfav,
                                 perm_add_localfav,
                                 perm_view_zoo,
                                 perm_change_zoo,
                                 perm_add_zoo,
                                 perm_view_hotel,
                                 perm_change_hotel,
                                 perm_add_hotel,
                                 perm_view_cuisine,
                                 perm_change_cuisine,
                                 perm_add_cuisine,
                                 perm_view_restaurant,
                                 perm_change_restaurant,
                                 perm_add_restaurant,
                                 perm_view_route,
                                 perm_change_route,
                                 perm_add_route,
                                 perm_view_city,
                                )

    my_groups_initialization_list = [
        {
            "name": "user",
            "permissions_list": user_permissions,
        },
        {
            "name": "reviewer",
            "permissions_list": reviewer_permissions,
        },
        {
            "name": "updater",
            "permissions_list": updater_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('sichuaninfo', '0006_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
