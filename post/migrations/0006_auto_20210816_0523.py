# Generated by Django 3.2.6 on 2021-08-15 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_post_send_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='authorname',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=100),
        ),
    ]
