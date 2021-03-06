# Generated by Django 3.1.7 on 2021-05-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=280)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('done', models.BooleanField()),
            ],
        ),
    ]
