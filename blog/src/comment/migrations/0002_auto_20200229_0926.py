# Generated by Django 2.2 on 2020-02-29 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'nazar', 'verbose_name_plural': 'nazarha'},
        ),
        migrations.AlterModelTable(
            name='comment',
            table='nazarat',
        ),
    ]
