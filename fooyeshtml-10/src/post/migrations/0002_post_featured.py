# Generated by Django 3.1.4 on 2023-02-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
