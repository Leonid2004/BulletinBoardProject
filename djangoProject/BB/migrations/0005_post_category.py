# Generated by Django 3.2.4 on 2021-07-16 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BB', '0004_alter_post_wholiked'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Category',
            field=models.CharField(default='Общее', max_length=20),
        ),
    ]
