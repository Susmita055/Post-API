# Generated by Django 4.1 on 2022-09-28 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendencemanagementsystems', '0007_user_groups_user_user_permissions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDetails',
            new_name='ContactDetails',
        ),
    ]
