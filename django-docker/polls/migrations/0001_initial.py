# Generated by Django 3.1.2 on 2022-01-30 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Claster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameClaster', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameProject', models.CharField(max_length=60)),
                ('course', models.CharField(max_length=4)),
                ('discription', models.TextField()),
                ('jobs', models.TextField()),
                ('supervisor', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=110)),
                ('image', models.FileField(upload_to='путь')),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.claster')),
            ],
        ),
    ]
