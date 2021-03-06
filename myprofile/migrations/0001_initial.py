# Generated by Django 3.0.8 on 2020-09-06 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=20)),
                ('school_year', models.IntegerField(default=0)),
                ('school_class', models.IntegerField(default=0)),
                ('intro', models.CharField(max_length=200)),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='USERNAME')),
            ],
        ),
    ]
