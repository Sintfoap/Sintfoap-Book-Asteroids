# Generated by Django 3.2.3 on 2021-07-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklibrary', '0008_auto_20210624_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
