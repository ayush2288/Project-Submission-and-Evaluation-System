# Generated by Django 5.1 on 2024-08-11 03:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('present', '0004_alter_sy_add_idea_no_sy_idea_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='final_idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='present.sy_add_idea_no')),
            ],
        ),
    ]
