# Generated by Django 4.2.4 on 2023-10-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_donorregister_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='donorregister',
            name='ldonation',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donorregister',
            name='dob',
            field=models.DateField(default='2003-12-24'),
            preserve_default=False,
        ),
    ]
