# Generated by Django 3.2.23 on 2023-12-08 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_rename_reviews_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]