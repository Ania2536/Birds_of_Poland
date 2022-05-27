# Generated by Django 4.0.3 on 2022-04-07 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds_app', '0011_alter_quiz_description_question_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title', models.CharField(max_length=150)),
                ('action_name', models.CharField(max_length=50)),
            ],
        ),
    ]