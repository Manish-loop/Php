# Generated by Django 5.0.7 on 2024-11-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateapplication',
            name='status',
            field=models.CharField(choices=[('pandding', 'pandding'), ('selected', 'selected')], default='pandding', max_length=20),
        ),
    ]
