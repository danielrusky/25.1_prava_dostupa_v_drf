# Generated by Django 4.2.10 on 2024-02-26 18:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_user_options_remove_user_username_user_avatar_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("member", "member"), ("moderator", "moderator")],
                default="member",
                max_length=20,
                verbose_name="роль",
            ),
        ),
    ]
