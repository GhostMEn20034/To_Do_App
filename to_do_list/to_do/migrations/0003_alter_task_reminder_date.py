# Generated by Django 4.1 on 2022-08-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0002_alter_task_reminder_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='reminder_date',
            field=models.DateTimeField(blank=True, default=''),
        ),
    ]