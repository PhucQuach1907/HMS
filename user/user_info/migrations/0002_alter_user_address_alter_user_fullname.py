# Generated by Django 5.0.6 on 2024-05-29 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_info.address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='fullname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_info.fullname'),
        ),
    ]