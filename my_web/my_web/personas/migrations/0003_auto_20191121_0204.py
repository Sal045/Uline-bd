# Generated by Django 2.2.7 on 2019-11-21 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('personas', '0002_auto_20191116_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='hermanos',
            field=models.ManyToManyField(to='personas.Persona'),
        ),
        migrations.CreateModel(
            name='Hermandad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona_dos',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_to_set',
                                   to='personas.Persona')),
                ('persona_uno',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_from_set',
                                   to='personas.Persona')),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='hermanos_new',
            field=models.ManyToManyField(related_name='mis_hermanos', through='personas.Hermandad',
                                         to='personas.Persona'),
        ),
    ]
