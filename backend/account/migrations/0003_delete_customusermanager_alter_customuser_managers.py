# Generated by Django 4.2.3 on 2023-08-02 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customusermanager_alter_customuser_managers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUserManager',
        ),
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
    ]
