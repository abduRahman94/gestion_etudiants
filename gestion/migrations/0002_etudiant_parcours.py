# Generated by Django 3.2 on 2022-08-10 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='parcours',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
