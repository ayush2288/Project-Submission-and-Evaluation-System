# Generated by Django 5.1 on 2024-08-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('present', '0019_alter_finalmarksevaluation_num1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='num1',
            field=models.CharField(choices=[('5', 'Cites substantial current quality literature(5)'), ('4', 'Cites reasonable quantity of current quality literature(4)'), ('3', 'Cites current literature(3)'), ('2', 'Does not cite any current quality literature(2)'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='num2',
            field=models.CharField(choices=[('5', 'Provides good understanding of literature cited(5)'), ('4', 'Provides understanding of literature cited(4)'), ('3', 'Exhibits poor understanding of literature cited(3)'), ('2', 'Very poor in understanding literature cited(2)'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='num21',
            field=models.CharField(choices=[('10', 'Very good clarity about the subject matter'), ('8', 'Somewhat good clarity'), ('6', 'Not so good clarity'), ('4', 'Very poor'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='num31',
            field=models.CharField(choices=[('3', 'Written in own, grammatically correct language'), ('2.4', 'Written in own language, has many grammatical errors'), ('1.8', 'Language not good'), ('1.2', 'Mostly copied'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='num32',
            field=models.CharField(choices=[('2', 'Recommended format used'), ('1.4', 'Mostly in recommended format'), ('1.2', 'Many deviations from format'), ('0.8', 'No format'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='num33',
            field=models.CharField(choices=[('3', 'Very good presentation'), ('2.4', 'Somewhat good presentation'), ('1.8', 'Messy presentation'), ('1.2', 'Very poor presentation'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='num34',
            field=models.CharField(choices=[('2', 'Very good Communication Skill'), ('1.4', 'Good Communication Skill'), ('1.2', 'Poor Communication Skill'), ('0.8', 'Very poor Communication Skill'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='num41',
            field=models.CharField(choices=[('10', 'International (Refereed) print Journal'), ('8', 'National (Refereed) print Journal'), ('6', 'International (Refereed) Conference'), ('4', 'National (Refereed) Conference and Online Journal'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='num51',
            field=models.CharField(choices=[('2.5', 'Highly effective communication'), ('2.0', 'Good communication'), ('1.5', 'Adequate communication'), ('1.0', 'Ineffective communication'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='num52',
            field=models.CharField(choices=[('2.5', 'Equal contribution from all members'), ('2.0', 'Good contribution from most members'), ('1.5', 'Uneven contribution'), ('1.0', 'Poor contribution from members'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='num53',
            field=models.CharField(choices=[('2.5', 'Excellent coordination'), ('2.0', 'Good coordination'), ('1.5', 'Adequate coordination'), ('1.0', 'Poor coordination'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='num54',
            field=models.CharField(choices=[('2.5', 'Excellent coordination'), ('2.0', 'Good coordination'), ('1.5', 'Adequate coordination'), ('1.0', 'Poor coordination'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p2_num1',
            field=models.CharField(choices=[('5', 'Cites substantial current quality literature(5)'), ('4', 'Cites reasonable quantity of current quality literature(4)'), ('3', 'Cites current literature(3)'), ('2', 'Does not cite any current quality literature(2)'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p2_num2',
            field=models.CharField(choices=[('5', 'Provides good understanding of literature cited(5)'), ('4', 'Provides understanding of literature cited(4)'), ('3', 'Exhibits poor understanding of literature cited(3)'), ('2', 'Very poor in understanding literature cited(2)'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p2_num21',
            field=models.CharField(choices=[('10', 'Very good clarity about the subject matter'), ('8', 'Somewhat good clarity'), ('6', 'Not so good clarity'), ('4', 'Very poor'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p2_num31',
            field=models.CharField(choices=[('3', 'Written in own, grammatically correct language'), ('2.4', 'Written in own language, has many grammatical errors'), ('1.8', 'Language not good'), ('1.2', 'Mostly copied'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p2_num32',
            field=models.CharField(choices=[('2', 'Recommended format used'), ('1.4', 'Mostly in recommended format'), ('1.2', 'Many deviations from format'), ('0.8', 'No format'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p2_num33',
            field=models.CharField(choices=[('3', 'Very good presentation'), ('2.4', 'Somewhat good presentation'), ('1.8', 'Messy presentation'), ('1.2', 'Very poor presentation'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p2_num34',
            field=models.CharField(choices=[('2', 'Very good Communication Skill'), ('1.4', 'Good Communication Skill'), ('1.2', 'Poor Communication Skill'), ('0.8', 'Very poor Communication Skill'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p2_num41',
            field=models.CharField(choices=[('10', 'International (Refereed) print Journal'), ('8', 'National (Refereed) print Journal'), ('6', 'International (Refereed) Conference'), ('4', 'National (Refereed) Conference and Online Journal'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p2_num51',
            field=models.CharField(choices=[('2.5', 'Highly effective communication'), ('2.0', 'Good communication'), ('1.5', 'Adequate communication'), ('1.0', 'Ineffective communication'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p2_num52',
            field=models.CharField(choices=[('2.5', 'Equal contribution from all members'), ('2.0', 'Good contribution from most members'), ('1.5', 'Uneven contribution'), ('1.0', 'Poor contribution from members'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p2_num53',
            field=models.CharField(choices=[('2.5', 'Excellent coordination'), ('2.0', 'Good coordination'), ('1.5', 'Adequate coordination'), ('1.0', 'Poor coordination'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p2_num54',
            field=models.CharField(choices=[('2.5', 'Excellent coordination'), ('2.0', 'Good coordination'), ('1.5', 'Adequate coordination'), ('1.0', 'Poor coordination'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p3_num1',
            field=models.CharField(choices=[('5', 'Cites substantial current quality literature(5)'), ('4', 'Cites reasonable quantity of current quality literature(4)'), ('3', 'Cites current literature(3)'), ('2', 'Does not cite any current quality literature(2)'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p3_num2',
            field=models.CharField(choices=[('5', 'Provides good understanding of literature cited(5)'), ('4', 'Provides understanding of literature cited(4)'), ('3', 'Exhibits poor understanding of literature cited(3)'), ('2', 'Very poor in understanding literature cited(2)'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p3_num21',
            field=models.CharField(choices=[('10', 'Very good clarity about the subject matter'), ('8', 'Somewhat good clarity'), ('6', 'Not so good clarity'), ('4', 'Very poor'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p3_num31',
            field=models.CharField(choices=[('3', 'Written in own, grammatically correct language'), ('2.4', 'Written in own language, has many grammatical errors'), ('1.8', 'Language not good'), ('1.2', 'Mostly copied'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p3_num32',
            field=models.CharField(choices=[('2', 'Recommended format used'), ('1.4', 'Mostly in recommended format'), ('1.2', 'Many deviations from format'), ('0.8', 'No format'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p3_num33',
            field=models.CharField(choices=[('3', 'Very good presentation'), ('2.4', 'Somewhat good presentation'), ('1.8', 'Messy presentation'), ('1.2', 'Very poor presentation'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p3_num34',
            field=models.CharField(choices=[('2', 'Very good Communication Skill'), ('1.4', 'Good Communication Skill'), ('1.2', 'Poor Communication Skill'), ('0.8', 'Very poor Communication Skill'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p3_num41',
            field=models.CharField(choices=[('10', 'International (Refereed) print Journal'), ('8', 'National (Refereed) print Journal'), ('6', 'International (Refereed) Conference'), ('4', 'National (Refereed) Conference and Online Journal'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p3_num51',
            field=models.CharField(choices=[('2.5', 'Highly effective communication'), ('2.0', 'Good communication'), ('1.5', 'Adequate communication'), ('1.0', 'Ineffective communication'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p3_num52',
            field=models.CharField(choices=[('2.5', 'Equal contribution from all members'), ('2.0', 'Good contribution from most members'), ('1.5', 'Uneven contribution'), ('1.0', 'Poor contribution from members'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p3_num53',
            field=models.CharField(choices=[('2.5', 'Excellent coordination'), ('2.0', 'Good coordination'), ('1.5', 'Adequate coordination'), ('1.0', 'Poor coordination'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p3_num54',
            field=models.CharField(choices=[('2.5', 'Excellent coordination'), ('2.0', 'Good coordination'), ('1.5', 'Adequate coordination'), ('1.0', 'Poor coordination'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p4_num1',
            field=models.CharField(choices=[('5', 'Cites substantial current quality literature(5)'), ('4', 'Cites reasonable quantity of current quality literature(4)'), ('3', 'Cites current literature(3)'), ('2', 'Does not cite any current quality literature(2)'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p4_num2',
            field=models.CharField(choices=[('5', 'Provides good understanding of literature cited(5)'), ('4', 'Provides understanding of literature cited(4)'), ('3', 'Exhibits poor understanding of literature cited(3)'), ('2', 'Very poor in understanding literature cited(2)'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p4_num21',
            field=models.CharField(choices=[('10', 'Very good clarity about the subject matter'), ('8', 'Somewhat good clarity'), ('6', 'Not so good clarity'), ('4', 'Very poor'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p4_num31',
            field=models.CharField(choices=[('3', 'Written in own, grammatically correct language'), ('2.4', 'Written in own language, has many grammatical errors'), ('1.8', 'Language not good'), ('1.2', 'Mostly copied'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p4_num32',
            field=models.CharField(choices=[('2', 'Recommended format used'), ('1.4', 'Mostly in recommended format'), ('1.2', 'Many deviations from format'), ('0.8', 'No format'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p4_num33',
            field=models.CharField(choices=[('3', 'Very good presentation'), ('2.4', 'Somewhat good presentation'), ('1.8', 'Messy presentation'), ('1.2', 'Very poor presentation'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p4_num34',
            field=models.CharField(choices=[('2', 'Very good Communication Skill'), ('1.4', 'Good Communication Skill'), ('1.2', 'Poor Communication Skill'), ('0.8', 'Very poor Communication Skill'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p4_num41',
            field=models.CharField(choices=[('10', 'International (Refereed) print Journal'), ('8', 'National (Refereed) print Journal'), ('6', 'International (Refereed) Conference'), ('4', 'National (Refereed) Conference and Online Journal'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p4_num51',
            field=models.CharField(choices=[('2.5', 'Highly effective communication'), ('2.0', 'Good communication'), ('1.5', 'Adequate communication'), ('1.0', 'Ineffective communication'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p4_num52',
            field=models.CharField(choices=[('2.5', 'Equal contribution from all members'), ('2.0', 'Good contribution from most members'), ('1.5', 'Uneven contribution'), ('1.0', 'Poor contribution from members'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p4_num53',
            field=models.CharField(choices=[('2.5', 'Excellent coordination'), ('2.0', 'Good coordination'), ('1.5', 'Adequate coordination'), ('1.0', 'Poor coordination'), ('0', 'bhak')], default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='finalmarksevaluation',
            name='p4_num54',
            field=models.CharField(choices=[('2.5', 'Excellent coordination'), ('2.0', 'Good coordination'), ('1.5', 'Adequate coordination'), ('1.0', 'Poor coordination'), ('0', 'bhak')], default='0', max_length=60),
        ),
    ]
