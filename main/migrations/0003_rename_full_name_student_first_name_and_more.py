# Generated by Django 4.2.11 on 2024-04-16 06:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_course_options_alter_coursecategory_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='full_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
