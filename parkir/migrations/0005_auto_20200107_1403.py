# Generated by Django 3.0.1 on 2020-01-07 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parkir', '0004_auto_20200107_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='parkir',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='parkir.tempatParkir'),
        ),
        migrations.AlterField(
            model_name='tempatparkir',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]