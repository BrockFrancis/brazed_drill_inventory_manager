# Generated by Django 4.1.4 on 2023-01-18 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diameter', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=20)),
                ('coating', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread', models.CharField(max_length=20)),
                ('casting', models.CharField(max_length=20)),
                ('center', models.CharField(max_length=20)),
                ('peripheral', models.CharField(max_length=20)),
                ('intermediate', models.CharField(max_length=20)),
                ('pad', models.CharField(max_length=20)),
                ('drill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.drill')),
            ],
        ),
    ]
