# Generated by Django 4.2 on 2023-05-09 19:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users_event", "0006_alter_tag_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="participant",
            name="sent_email",
            field=models.BooleanField(default=False),
        ),
    ]
