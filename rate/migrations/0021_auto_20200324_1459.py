# Generated by Django 3.0.4 on 2020-03-24 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0020_auto_20200324_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='category',
            field=models.CharField(choices=[('Comment', 'Comment'), ('Report', 'Report'), ('Login', 'Login'), ('Logout', 'Logout'), ('Signup', 'Signup'), ('Like', 'Like'), ('Disike', 'Dislike')], max_length=50),
        ),
    ]