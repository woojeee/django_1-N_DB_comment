# Generated by Django 2.2 on 2019-04-30 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookreviewapp', '0005_comment_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=200),
        ),
    ]