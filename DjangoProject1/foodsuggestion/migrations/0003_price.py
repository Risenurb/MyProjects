# Generated by Django 4.1 on 2022-09-09 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodsuggestion', '0002_foodsuggestion_price_range'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_range1', models.CharField(max_length=70)),
                ('price_range1_name', models.CharField(max_length=100)),
            ],
        ),
    ]
