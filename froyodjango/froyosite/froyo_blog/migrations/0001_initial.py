# Generated by Django 4.0.4 on 2022-05-31 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=60)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
