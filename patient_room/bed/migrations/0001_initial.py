# Generated by Django 4.1.13 on 2024-06-02 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_number', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('patient_id', models.PositiveIntegerField(blank=True, null=True)),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
            ],
            options={
                'db_table': 'patient_bed',
            },
        ),
    ]