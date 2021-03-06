# Generated by Django 4.0.3 on 2022-03-29 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('birds_app', '0002_images_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='birds',
            name='family',
        ),
        migrations.AddField(
            model_name='family',
            name='family',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='birds_app.birds'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
