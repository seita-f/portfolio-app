# Generated by Django 3.1.7 on 2022-02-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20220222_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=20)),
                ('percentage', models.CharField(max_length=5)),
            ],
        ),
    ]
