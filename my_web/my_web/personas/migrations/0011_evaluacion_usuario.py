# Generated by Django 2.2.7 on 2019-11-30 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0010_remove_evaluacion_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluacion_de_los_usario', to='personas.Usuario'),
        ),
    ]