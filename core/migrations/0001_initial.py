# Generated by Django 4.1rc1 on 2022-07-29 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Boat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("capacity", models.IntegerField()),
                ("captain_name", models.CharField(max_length=100)),
                (
                    "captain_certificaiton",
                    models.CharField(default="", max_length=1000),
                ),
                ("captain_photo", models.ImageField(upload_to="captains/")),
                ("deckhand_name", models.CharField(max_length=100)),
                ("deckhand_photo", models.ImageField(upload_to="deckhand/")),
                ("niwa_approval_date", models.DateField()),
                ("laswa_approval_date", models.DateField()),
                ("certification_status", models.CharField(default="", max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="Operator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("contact_info", models.CharField(max_length=255)),
                ("operation_commenced", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reviewer_name", models.CharField(max_length=100)),
                ("rating", models.IntegerField()),
                ("content", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "boat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.boat"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="boat",
            name="operator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.operator"
            ),
        ),
    ]
