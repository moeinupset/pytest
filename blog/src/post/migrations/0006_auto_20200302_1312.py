# Generated by Django 2.2 on 2020-03-02 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20200301_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='post', to='category.Category'),
        ),
    ]
