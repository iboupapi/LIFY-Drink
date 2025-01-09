# Generated by Django 5.1.4 on 2025-01-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.CharField(choices=[('CL', 'Classique'), ('PM', 'Premium'), ('GD', 'Gold')], default='', max_length=5),
            preserve_default=False,
        ),
    ]
