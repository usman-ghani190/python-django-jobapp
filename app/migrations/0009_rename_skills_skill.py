# Generated by Django 5.1.1 on 2024-10-04 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_skills_jobpost_skills'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
    ]
