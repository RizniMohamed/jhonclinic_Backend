# Generated by Django 4.1 on 2022-08-06 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('image', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('recordID', models.AutoField(primary_key=True, serialize=False)),
                ('disease', models.CharField(max_length=100)),
                ('diagnosis', models.CharField(max_length=500)),
                ('prescription', models.JSONField()),
                ('date', models.CharField(max_length=150)),
                ('payment', models.BigIntegerField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
    ]
