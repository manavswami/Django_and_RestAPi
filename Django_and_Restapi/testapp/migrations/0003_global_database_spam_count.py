# Generated by Django 2.2.7 on 2019-11-18 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20191118_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='global_database',
            name='spam_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
