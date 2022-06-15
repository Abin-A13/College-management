# Generated by Django 4.0.5 on 2022-06-14 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_hod_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='admission_number',
            field=models.CharField(default=34, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='students',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1),
        ),
    ]
