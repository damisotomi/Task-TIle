# Generated by Django 4.1.7 on 2023-03-21 19:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('launch_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(1, 'Live'), (2, 'Pending'), (3, 'Archived')], default=2)),
            ],
            options={
                'ordering': ['launch_date'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('order', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.IntegerField(blank=True, choices=[(1, 'Survey'), (2, 'Discussion'), (3, 'Diary')], null=True)),
                ('tile', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='tasks', to='tasktileapp.tile')),
            ],
        ),
    ]
