# Generated by Django 3.2.5 on 2021-12-05 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='shortdesc',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]