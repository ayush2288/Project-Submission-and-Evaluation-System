# Generated by Django 5.0.1 on 2024-08-29 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('present', '0025_alter_finalmarksevaluation_final_marks_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='final_marks_student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='present.sy_idea_no'),
        ),
    ]
