# Generated by Django 4.0.4 on 2022-06-02 17:39

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentecobre', '0005_alter_articulos_universo_alter_glosario_universo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulos',
            name='enlacecopperen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='glosario',
            name='universo',
            field=models.CharField(blank=True, choices=[('A', 'Aliento de los dioses'), ('AB', 'Arena Blanca'), ('AE', 'El alma del emperador'), ('AL', 'Alcatraz'), ('C', 'Cosmere'), ('CT', 'Citoverso'), ('E', 'Elantris'), ('FU', 'Fuera del universo'), ('L', 'Legión'), ('M', 'Nacidos de la bruma'), ('OH', 'Otras Historias'), ('R', 'Rithmatista'), ('RK', 'Reckoners'), ('RT', 'Rueda del Tiempo'), ('S', 'Archivo de las tormentas'), ('SO', 'Sexto del Ocaso'), ('SS', 'Sombras por silencio')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='universo',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('A', 'Aliento de los dioses'), ('AB', 'Arena Blanca'), ('AE', 'El alma del emperador'), ('AL', 'Alcatraz'), ('C', 'Cosmere'), ('CT', 'Citoverso'), ('E', 'Elantris'), ('FU', 'Fuera del universo'), ('L', 'Legión'), ('M', 'Nacidos de la bruma'), ('OH', 'Otras Historias'), ('R', 'Rithmatista'), ('RK', 'Reckoners'), ('RT', 'Rueda del Tiempo'), ('S', 'Archivo de las tormentas'), ('SO', 'Sexto del Ocaso'), ('SS', 'Sombras por silencio')], max_length=100, null=True),
        ),
    ]
