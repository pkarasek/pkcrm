# Generated by Django 2.0.3 on 2018-04-03 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crms', '0005_auto_20180402_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_contact',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
