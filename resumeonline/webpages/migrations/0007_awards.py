# Generated by Django 4.0.3 on 2022-03-20 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0006_remove_education_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_name', models.CharField(max_length=100)),
                ('awarded_by', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
