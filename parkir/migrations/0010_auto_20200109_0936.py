# Generated by Django 3.0.1 on 2020-01-09 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkir', '0009_auto_20200109_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='parkir',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='parkir.tempatParkir'),
        ),
    ]