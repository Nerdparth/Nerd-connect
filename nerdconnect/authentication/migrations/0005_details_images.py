# Generated by Django 5.1.2 on 2024-10-13 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_details_lname'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='images',
            field=models.ImageField(default='default.jpg', upload_to='profile-photo/'),
        ),
    ]
