# Generated by Django 4.0.2 on 2022-02-20 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0003_remove_track_artists_track_artists'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('release_date', models.DateField()),
                ('type', models.CharField(default='Album', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='track',
            name='albums',
            field=models.ManyToManyField(related_name='tracks', to='spotify.Artist'),
        ),
    ]
