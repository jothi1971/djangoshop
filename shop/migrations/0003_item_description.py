# Generated by Django 2.1.3 on 2020-04-02 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200402_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
