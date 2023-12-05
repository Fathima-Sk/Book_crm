# Generated by Django 4.2.6 on 2023-11-27 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0003_delete_student_employee_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254, null=True)),
                ('gender', models.CharField(max_length=10)),
                ('place', models.CharField(max_length=30)),
            ],
        ),
    ]
