# Generated by Django 2.2.6 on 2019-10-26 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_film_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='man',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_men', to=settings.AUTH_USER_MODEL),
        ),
    ]
