# Generated by Django 4.1.2 on 2022-12-13 22:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('desactivate', models.BooleanField(default=False)),
                ('image', models.ImageField(null=True, upload_to='media/images_news/')),
                ('cathegory', models.CharField(max_length=100)),
            ],
        ),
    ]
