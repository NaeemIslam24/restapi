# Generated by Django 4.0 on 2021-12-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_remove_agent_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='image',
            field=models.ImageField(default=1, upload_to='realtor'),
            preserve_default=False,
        ),
    ]