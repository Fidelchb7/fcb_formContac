# Generated by Django 4.0.6 on 2023-03-22 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcb_ContacFormApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='estado',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]