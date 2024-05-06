# Generated by Django 3.2.25 on 2024-05-05 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('post', models.TextField()),
                ('thumbnail', models.ImageField(default='', upload_to='images/')),
            ],
        ),
    ]
