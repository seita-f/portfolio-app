# Generated by Django 3.1.7 on 2022-02-22 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20220222_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=30)),
                ('text', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
    ]