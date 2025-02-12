# Generated by Django 5.1.6 on 2025-02-10 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('damage', models.IntegerField()),
                ('accuracy', models.FloatField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Moveset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_move', models.ManyToManyField(related_name='first_move', to='duck.move')),
                ('fourth_move', models.ManyToManyField(related_name='fourth_move', to='duck.move')),
                ('second_move', models.ManyToManyField(related_name='second_move', to='duck.move')),
                ('third_move', models.ManyToManyField(related_name='third_move', to='duck.move')),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('moveset', models.ManyToManyField(related_name='moveset', to='duck.moveset')),
            ],
        ),
    ]
