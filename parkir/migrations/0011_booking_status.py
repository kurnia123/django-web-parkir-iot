# Generated by Django 3.0.1 on 2020-01-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkir', '0010_auto_20200109_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
