# Generated by Django 4.1.5 on 2023-01-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='main_site.tag'),
        ),
    ]
