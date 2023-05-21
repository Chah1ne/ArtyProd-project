# Generated by Django 4.1.7 on 2023-05-16 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('Design Graphique', 'Design Graphique'), ('Design Web', 'Design Web'), ('SC', 'Scénarisation')], max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('acheve', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, upload_to='media/')),
                ('equipe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artyweb.equipe')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artyweb.service')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('cv', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
                ('lien_fb', models.URLField(blank=True, null=True)),
                ('equipe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artyweb.equipe')),
            ],
        ),
    ]