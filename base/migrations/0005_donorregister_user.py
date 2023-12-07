# Generated by Django 4.2.4 on 2023-11-07 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_donorregister_ldonation_alter_donorregister_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='donorregister',
            name='user',
            field=models.ForeignKey(default=18, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]