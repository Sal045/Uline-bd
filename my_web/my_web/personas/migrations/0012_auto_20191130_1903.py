# Generated by Django 2.2.7 on 2019-11-30 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0011_evaluacion_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluaciones_de_curso', to='personas.Curso'),
        ),
    ]
