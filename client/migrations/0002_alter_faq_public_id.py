# Generated by Django 4.1.5 on 2023-01-14 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='public_id',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
