# Generated by Django 3.0.3 on 2020-09-29 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='massege',
            new_name='message',
        ),
    ]
