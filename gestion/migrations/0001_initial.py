# Generated by Django 3.2 on 2022-07-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
