# Generated by Django 3.1.4 on 2021-04-30 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("codechallenges", "0003_submission_answer"),
    ]

    operations = [
        migrations.AddField(
            model_name="submission",
            name="attempts",
            field=models.IntegerField(default=0),
        ),
    ]