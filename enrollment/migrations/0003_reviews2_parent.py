# Generated by Django 3.0.7 on 2020-08-01 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0002_auto_20200731_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews2',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='enrollment.Reviews2', verbose_name='Родитель'),
        ),
    ]
