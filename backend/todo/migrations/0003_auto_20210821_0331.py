# Generated by Django 3.1.2 on 2021-08-21 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.IntegerField(default=1)),
                ('destination', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='x',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='todo',
            name='y',
            field=models.FloatField(default=1.0),
        ),
    ]
