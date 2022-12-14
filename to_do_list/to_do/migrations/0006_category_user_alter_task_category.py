# Generated by Django 4.1 on 2022-10-29 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('to_do', '0005_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(default='My day', on_delete=django.db.models.deletion.CASCADE, to='to_do.category'),
        ),
    ]
