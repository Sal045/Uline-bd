# Generated by Django 2.2.7 on 2019-11-21 02:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('personas', '0004_remove_persona_hermanos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='hermanos_new',
        ),
        migrations.AddField(
            model_name='persona',
            name='hermanos',
            field=models.ManyToManyField(related_name='mis_hermanos', through='personas.Hermandad',
                                         to='personas.Persona'),
        ),
    ]
