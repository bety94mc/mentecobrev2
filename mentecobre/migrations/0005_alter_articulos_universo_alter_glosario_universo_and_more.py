# Generated by Django 4.0b1 on 2022-05-26 11:41

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentecobre', '0004_alter_usuario_universo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='universo',
            field=models.CharField(blank=True, choices=[('C', 'Cosmere'), ('M', 'Mistborn'), ('S', 'Stormlight'), ('A', 'Aliento'), ('E', 'Elantris'), ('AB', 'Arena Blanca'), ('B', 'Brandon'), ('FU', 'Fuera Universo'), ('OH', 'Otras Historias'), ('R', 'Rithmatista'), ('RT', 'Rueda del Tiempo'), ('CT', 'Citoverso'), ('RK', 'Reckoners'), ('SS', 'Sombras por Silencio'), ('AL', 'Alcatraz'), ('L', 'Legion'), ('SO', 'Sexto del Ocaso'), ('AE', 'Alma del Emperador')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='glosario',
            name='universo',
            field=models.CharField(blank=True, choices=[('A', 'Aliento de los diosos'), ('AB', 'Arena Blanca'), ('AE', 'El alma del emperador'), ('AL', 'Alcatraz'), ('C', 'Cosmere'), ('CT', 'Citoverso'), ('E', 'Elantris'), ('FU', 'Fuera del universo'), ('L', 'Legión'), ('M', 'Nacidos de la bruma'), ('OH', 'Otras Historias'), ('R', 'Rithmatista'), ('RK', 'Reckoners'), ('RT', 'Rueda del Tiempo'), ('S', 'Archivo de las tormentas'), ('SO', 'Sexto del Ocaso'), ('SS', 'Sombras por silencio')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='universo',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('A', 'Aliento de los diosos'), ('AB', 'Arena Blanca'), ('AE', 'El alma del emperador'), ('AL', 'Alcatraz'), ('C', 'Cosmere'), ('CT', 'Citoverso'), ('E', 'Elantris'), ('FU', 'Fuera del universo'), ('L', 'Legión'), ('M', 'Nacidos de la bruma'), ('OH', 'Otras Historias'), ('R', 'Rithmatista'), ('RK', 'Reckoners'), ('RT', 'Rueda del Tiempo'), ('S', 'Archivo de las tormentas'), ('SO', 'Sexto del Ocaso'), ('SS', 'Sombras por silencio')], max_length=100, null=True),
        ),
    ]