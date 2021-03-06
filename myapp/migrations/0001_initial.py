# Generated by Django 4.0.5 on 2022-06-14 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=154)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=15)),
                ('locality', models.CharField(max_length=154)),
                ('city', models.CharField(max_length=154)),
                ('pin', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('pradesh1', 'pradesh1'), ('pradesh2', 'pradesh2'), ('pradesh3', 'pradesh3'), ('pradesh4', 'pradesh4'), ('pradesh5', 'pradesh5'), ('pradesh6', 'pradesh6'), ('pradesh7', 'pradesh7')], max_length=154)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('job_city', models.CharField(max_length=154)),
                ('profile_image', models.ImageField(blank=True, upload_to='profileimg')),
                ('my_file', models.FileField(blank=True, upload_to='doc')),
            ],
        ),
    ]
