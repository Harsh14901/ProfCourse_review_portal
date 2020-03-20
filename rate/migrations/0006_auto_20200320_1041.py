# Generated by Django 3.0.4 on 2020-03-20 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0005_auto_20200320_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rate.Courses'),
        ),
        migrations.AlterField(
            model_name='review',
            name='prof',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rate.Profs'),
        ),
    ]