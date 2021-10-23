# Generated by Django 3.2 on 2021-05-20 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.FloatField()),
                ('Medu', models.FloatField()),
                ('Fedu', models.FloatField()),
                ('failures', models.FloatField()),
                ('freetime', models.FloatField()),
                ('goout', models.FloatField()),
                ('Walc', models.FloatField()),
                ('absences', models.FloatField()),
                ('G1', models.FloatField()),
                ('G2', models.FloatField()),
                ('classification', models.CharField(max_length=15)),
            ],
        ),
    ]
