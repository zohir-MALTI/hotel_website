# Generated by Django 3.0 on 2021-05-18 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('company', models.FloatField()),
                ('location', models.TextField()),
                ('salary', models.TextField()),
                ('link', models.URLField(unique=True)),
                ('category', models.IntegerField(choices=[('Reception', ((11, 'Réceptionniste'), (12, 'Chef de réception'))), ('Salle', ((21, "Maître d'hôtel"), (22, 'Serveur(se)'), (23, 'Sommelier'), (24, 'Barman'))), ('Entretien', ((31, 'Femme de chambre'), (32, 'Maçon'), (33, 'Plombier'), (34, 'Electricien'))), ('Restauration', ((41, 'Cuisinier'), (42, 'Chef de cuisine'), (43, 'Patissier'))), ('Sécurité', ((51, 'Agent de sécurité'), (52, 'Chef de sécurité'), (53, 'Spécialiste caméras')))], unique=True)),
                ('contract_type', models.CharField(choices=[('CDI', 'CDI'), ('CDD', 'CDD'), ('SAIS', 'Saisonier')], max_length=4)),
                ('description', models.TextField(blank=True)),
                ('job_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_date', models.DateTimeField(auto_now_add=True)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
