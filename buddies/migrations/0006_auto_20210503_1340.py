# Generated by Django 3.1.6 on 2021-05-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddies', '0005_auto_20210501_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='in_person',
            field=models.CharField(max_length=64, null=True),
        ),
    ]