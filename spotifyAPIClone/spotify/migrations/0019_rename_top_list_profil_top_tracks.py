# Generated by Django 4.0.2 on 2022-02-21 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0018_alter_profil_followers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profil',
            old_name='top_list',
            new_name='top_tracks',
        ),
    ]
