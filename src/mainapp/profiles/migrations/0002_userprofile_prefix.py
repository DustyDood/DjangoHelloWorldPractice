# Generated by Django 3.1.4 on 2020-12-10 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='prefix',
            field=models.CharField(choices=[('Mrs.', 'Mrs.'), ('Ms.', 'Ms'), ('Miss', 'Miss'), ('Mr.', 'Mr.')], default='Mr.', max_length=10),
            preserve_default=False,
        ),
    ]
