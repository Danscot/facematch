# Generated by Django 5.0.6 on 2024-07-02 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='points',
            new_name='votes',
        ),
        migrations.RemoveField(
            model_name='image',
            name='path',
        ),
    ]