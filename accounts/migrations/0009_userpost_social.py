# Generated by Django 4.2 on 2023-04-03 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_userpost_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='social',
            field=models.URLField(blank=True, null=True),
        ),
    ]
