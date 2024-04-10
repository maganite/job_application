# Generated by Django 4.2.11 on 2024-04-10 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('recent_degree', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('currently_working', models.BooleanField(default=False)),
                ('current_ctc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('eligible', models.BooleanField(default=False)),
            ],
        ),
    ]
