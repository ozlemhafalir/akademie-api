# Generated by Django 4.2.5 on 2023-10-09 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image_alter_profile_owner'),
        ('instructors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to='profiles.profile'),
        ),
    ]