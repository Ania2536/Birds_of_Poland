# Generated by Django 4.0.3 on 2022-03-30 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('birds_app', '0003_remove_birds_family_family_family_alter_images_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family',
            name='family',
        ),
        migrations.AddField(
            model_name='birds',
            name='family',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='birds_app.family'),
        ),
    ]
