# Generated by Django 4.1.7 on 2023-04-22 12:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Rakendus', '0002_tehing_andja_alter_tehing_saaja'),
    ]

    operations = [
        migrations.AddField(
            model_name='tehing',
            name='aeg',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Tehingu toimumise aeg'),
            preserve_default=False,
        ),
    ]
