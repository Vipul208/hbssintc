# Generated by Django 4.0.6 on 2022-08-02 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='galleries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gal')),
            ],
        ),
        migrations.CreateModel(
            name='noticeboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='teacher')),
                ('mail', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('heading', models.CharField(max_length=50)),
                ('dis', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]