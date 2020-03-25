# Generated by Django 3.0.4 on 2020-03-10 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=30)),
                ('car_model', models.CharField(max_length=30)),
                ('car_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateField()),
                ('drop_date', models.DateField()),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bondarev_app.Car')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('passport_id', models.IntegerField()),
                ('owners_car', models.ManyToManyField(through='bondarev_app.Document', to='bondarev_app.Car')),
            ],
        ),
        migrations.CreateModel(
            name='DriverLicense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_type', models.CharField(choices=[('G', 'Global'), ('L', 'Local')], max_length=1)),
                ('license_date', models.DateField()),
                ('License_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bondarev_app.Owner')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bondarev_app.Owner'),
        ),
    ]
