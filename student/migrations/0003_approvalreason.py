# Generated by Django 4.2 on 2023-05-23 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0002_remove_student_student_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="ApprovalReason",
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
                ("reason", models.TextField()),
                (
                    "student",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="student.student",
                    ),
                ),
            ],
        ),
    ]
