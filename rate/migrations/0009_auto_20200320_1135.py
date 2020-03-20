# Generated by Django 3.0.4 on 2020-03-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0008_auto_20200320_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='attendance',
            field=models.IntegerField(choices=[(0, 'Poor'), (1, 'Bad'), (2, 'Average'), (3, 'Above Average'), (4, 'Good'), (5, 'Excellent')], default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='content_quality',
            field=models.IntegerField(choices=[(0, 'Poor'), (1, 'Bad'), (2, 'Average'), (3, 'Above Average'), (4, 'Good'), (5, 'Excellent')], default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='difficulty',
            field=models.IntegerField(choices=[(0, 'Poor'), (1, 'Bad'), (2, 'Average'), (3, 'Above Average'), (4, 'Good'), (5, 'Excellent')], default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='grading',
            field=models.IntegerField(choices=[(0, 'Poor'), (1, 'Bad'), (2, 'Average'), (3, 'Above Average'), (4, 'Good'), (5, 'Excellent')], default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='overall_rating',
            field=models.IntegerField(choices=[(0, 'Poor'), (1, 'Bad'), (2, 'Average'), (3, 'Above Average'), (4, 'Good'), (5, 'Excellent')], default=0),
        ),
    ]