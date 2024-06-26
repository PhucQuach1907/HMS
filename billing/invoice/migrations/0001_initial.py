# Generated by Django 4.1.13 on 2024-05-30 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.PositiveIntegerField()),
                ('appointment_id', models.PositiveIntegerField()),
                ('price', models.PositiveBigIntegerField()),
                ('status', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'invoice',
            },
        ),
    ]
