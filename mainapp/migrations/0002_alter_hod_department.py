# Generated by Django 4.0.5 on 2022-06-14 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hod',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.department'),
        ),
    ]