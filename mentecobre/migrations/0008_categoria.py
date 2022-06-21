# Generated by Django 4.0.4 on 2022-06-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentecobre', '0007_usuario_notas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catEn', models.CharField(max_length=200)),
                ('catEs', models.CharField(blank=True, max_length=200, null=True)),
                ('urlEn', models.URLField(blank=True, max_length=2000, null=True)),
                ('urlEs', models.URLField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]
