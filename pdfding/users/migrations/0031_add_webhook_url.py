"""Add webhook_url field to Profile model

Revision ID: 0031
Revises: 0030
Create Date: 2026-05-01 22:44:00.000000

"""
from django.db import migrations, models


class Migration(migrations.Migration):
    """Migration to add webhook_url field to Profile model"""

    dependencies = [
        ('users', '0030_add_language_adjust_theme_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='webhook_url',
            field=models.URLField(blank=True, null=True, help_text='Webhook URL for PDF page updates'),
        ),
    ]