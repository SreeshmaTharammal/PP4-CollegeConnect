# Generated by Django 4.2.13 on 2024-07-01 11:42

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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('nationality', models.CharField(choices=[('US', 'United States'), ('CA', 'Canada'), ('GB', 'United Kingdom'), ('FR', 'France'), ('DE', 'Germany')], max_length=2)),
                ('phone_number', models.CharField(max_length=15)),
                ('emergency_contact_number', models.CharField(max_length=15)),
                ('is_student', models.BooleanField(default=False)),
                ('is_instructor', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_guest', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
