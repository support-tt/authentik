# Generated by Django 3.2 on 2021-04-16 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_sources_oauth", "0002_auto_20200520_1108"),
    ]

    operations = [
        migrations.AlterField(
            model_name="oauthsource",
            name="access_token_url",
            field=models.CharField(
                blank=True,
                help_text="URL used by authentik to retrive tokens.",
                max_length=255,
                verbose_name="Access Token URL",
            ),
        ),
        migrations.AlterField(
            model_name="oauthsource",
            name="authorization_url",
            field=models.CharField(
                blank=True,
                help_text="URL the user is redirect to to conest the flow.",
                max_length=255,
                verbose_name="Authorization URL",
            ),
        ),
        migrations.AlterField(
            model_name="oauthsource",
            name="profile_url",
            field=models.CharField(
                blank=True,
                help_text="URL used by authentik to get user information.",
                max_length=255,
                verbose_name="Profile URL",
            ),
        ),
    ]
