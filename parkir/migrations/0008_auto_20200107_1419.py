# Generated by Django 3.0.1 on 2020-01-07 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkir', '0007_auto_20200107_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='parkir',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parkir.tempatParkir'),
        ),
    ]
