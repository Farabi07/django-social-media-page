# Generated by Django 4.0.6 on 2022-07-18 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_login', '0002_alter_userprofile_profile_pic_alter_userprofile_dob_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True, max_length=264),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]
