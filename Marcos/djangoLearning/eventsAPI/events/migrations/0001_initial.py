# Generated by Django 3.1.1 on 2020-09-06 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('event', models.CharField(max_length=80)),
                ('priority', models.CharField(choices=[('0', 'Sem prioridade'), ('1', 'Normal'), ('2', 'Urgente'), ('3', 'Muito Urgente')], max_length=1)),
            ],
        ),
    ]
