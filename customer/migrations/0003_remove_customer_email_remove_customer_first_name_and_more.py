# Generated by Django 5.0 on 2024-01-03 13:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "customer",
            "0002_remove_purchaseoffer_color_alter_customer_created_at_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="email",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="username",
        ),
        migrations.AddField(
            model_name="customer",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
            preserve_default=False,
        ),
    ]