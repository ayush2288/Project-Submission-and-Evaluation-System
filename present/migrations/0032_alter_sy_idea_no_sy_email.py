# Generated by Django 5.1 on 2024-09-04 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('present', '0031_sy_idea_no_sy_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sy_idea_no',
            name='sy_email',
            field=models.CharField(default='@somaiya.edu', max_length=100),
        ),
    ]
