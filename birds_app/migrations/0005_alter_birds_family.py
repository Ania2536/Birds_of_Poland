# Generated by Django 4.0.3 on 2022-03-30 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('birds_app', '0004_remove_family_family_birds_family'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birds',
            name='family',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='birds_app.family'),
        ),
    ]
