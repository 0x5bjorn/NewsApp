# Generated by Django 4.0.3 on 2022-03-21 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_news_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='images',
            field=models.BinaryField(blank=True, editable=True),
        ),
    ]