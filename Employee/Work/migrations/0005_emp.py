# Generated by Django 4.2.6 on 2023-11-28 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0004_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=30)),
                ('salary', models.PositiveIntegerField()),
                ('contact', models.IntegerField()),
            ],
        ),
    ]
