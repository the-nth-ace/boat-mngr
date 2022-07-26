# Generated by Django 4.1rc1 on 2022-08-03 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_review_options_alter_boat_unique_together"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="boat",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="operator",
            options={"ordering": ["name"]},
        ),
        migrations.RemoveField(
            model_name="review",
            name="rating",
        ),
        migrations.RemoveField(
            model_name="review",
            name="reviewer_name",
        ),
    ]
