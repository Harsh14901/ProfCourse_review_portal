# Generated by Django 3.0.4 on 2020-03-23 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rate', '0016_auto_20200322_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Comment', 'Comment'), ('Report', 'Report'), ('Login', 'Login'), ('Logout', 'Logout'), ('Signup', 'Signup')], max_length=50)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('log', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
