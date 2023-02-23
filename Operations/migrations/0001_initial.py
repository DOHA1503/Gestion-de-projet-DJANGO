# Generated by Django 3.2.3 on 2021-07-08 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0006_auto_20210707_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField(null=True)),
                ('desc', models.TextField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Operations.category')),
                ('employe', models.ManyToManyField(to='accounts.Employe')),
            ],
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('duration', models.IntegerField()),
                ('desc', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[(0, 'open'), (1, 'running'), (2, 'paused'), (3, 'done')], default=0, max_length=1)),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Operations.projet')),
            ],
        ),
        migrations.CreateModel(
            name='RessourceMateriel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=200)),
                ('tache', models.ManyToManyField(to='Operations.Tache')),
            ],
        ),
    ]
