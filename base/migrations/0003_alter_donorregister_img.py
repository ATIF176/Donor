# Generated by Django 4.2.4 on 2023-10-14 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_donorregister_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorregister',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]