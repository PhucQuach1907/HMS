# Generated by Django 5.0.6 on 2024-05-30 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('specialty', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
    ]