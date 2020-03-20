# Generated by Django 3.0.4 on 2020-03-20 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0003_auto_20200319_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='attendance',
            field=models.PositiveSmallIntegerField(choices=[('Poor', 1), ('Bad', 2), ('Average', 3), ('Good', 4), ('Excellent', 5)], max_length=20),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(max_length=4096),
        ),
        migrations.AlterField(
            model_name='review',
            name='content_quality',
            field=models.PositiveSmallIntegerField(choices=[('Poor', 1), ('Bad', 2), ('Average', 3), ('Good', 4), ('Excellent', 5)], max_length=20),
        ),
        migrations.AlterField(
            model_name='review',
            name='difficulty',
            field=models.PositiveSmallIntegerField(choices=[('Poor', 1), ('Bad', 2), ('Average', 3), ('Good', 4), ('Excellent', 5)], max_length=20),
        ),
        migrations.AlterField(
            model_name='review',
            name='grading',
            field=models.PositiveSmallIntegerField(choices=[('Poor', 1), ('Bad', 2), ('Average', 3), ('Good', 4), ('Excellent', 5)], max_length=20),
        ),
        migrations.AlterField(
            model_name='review',
            name='overall_rating',
            field=models.PositiveSmallIntegerField(choices=[('Poor', 1), ('Bad', 2), ('Average', 3), ('Good', 4), ('Excellent', 5)], max_length=20),
        ),
    ]
