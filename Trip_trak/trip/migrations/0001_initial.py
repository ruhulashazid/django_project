# Generated by Django 4.0.6 on 2022-07-11 19:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=2)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='notes')),
                ('rating', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5)])),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='trip.trip')),
            ],
        ),
    ]