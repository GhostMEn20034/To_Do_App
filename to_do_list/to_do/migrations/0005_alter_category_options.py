# Generated by Django 4.1 on 2022-10-21 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0004_alter_task_reminder_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]