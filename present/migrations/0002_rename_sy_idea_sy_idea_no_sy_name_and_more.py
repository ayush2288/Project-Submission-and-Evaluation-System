# Generated by Django 5.0.1 on 2024-08-08 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('present', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sy_idea_no',
            old_name='sy_idea',
            new_name='sy_name',
        ),
        migrations.RemoveField(
            model_name='sy_idea_no',
            name='sy_grp_no',
        ),
        migrations.AddField(
            model_name='sy_idea_no',
            name='sy_group_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sy_idea_no',
            name='sy_roll_no',
            field=models.IntegerField(default=0),
        ),
    ]
