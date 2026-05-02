"""Add webhook_apikey and webhook_userid fields to Profile model

Revision ID: 0032
Revises: 0031
Create Date: 2026-05-02 16:59:00.000000

"""
from django.db import migrations, models


class Migration(migrations.Migration):
    """Migration to add webhook_apikey and webhook_userid fields to Profile model"""

    dependencies = [
        ('users', '0031_add_webhook_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='webhook_apikey',
            field=models.CharField(max_length=255, blank=True, null=True, help_text='Webhook API key for authentication'),
        ),
        migrations.AddField(
            model_name='profile',
            name='webhook_userid',
            field=models.CharField(max_length=255, blank=True, null=True, help_text='Webhook user ID for authentication'),
        ),
    ]