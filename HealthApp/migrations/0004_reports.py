# Generated by Django 4.2 on 2023-08-26 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("HealthApp", "0003_doctor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reports",
            fields=[
                ("report_no", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.DateField()),
                ("test_name", models.CharField(max_length=100)),
                (
                    "lab",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="HealthApp.lab"
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HealthApp.patient",
                    ),
                ),
            ],
        ),
    ]
