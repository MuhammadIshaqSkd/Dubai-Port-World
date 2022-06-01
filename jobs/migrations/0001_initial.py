# Generated by Django 4.0.2 on 2022-06-01 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ad_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('pub_date', models.DateField()),
                ('Ad_image', models.ImageField(default='', upload_to='DubaiPortWorld/media')),
            ],
        ),
    ]