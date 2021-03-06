# Generated by Django 3.2.3 on 2021-05-20 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booklibrary', '0005_auto_20210410_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('notes', models.CharField(blank=True, max_length=5000, null=True)),
                ('arrangers', models.ManyToManyField(related_name='songs_arranged', to='booklibrary.People')),
                ('composers', models.ManyToManyField(related_name='songs_composed', to='booklibrary.People')),
                ('lyricists', models.ManyToManyField(related_name='songs_lirisized', to='booklibrary.People')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='songs', to='booklibrary.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='DateSung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booklibrary.song')),
            ],
        ),
    ]
