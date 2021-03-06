# Generated by Django 3.0 on 2021-05-19 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20210518_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
                ('firstname', models.TextField()),
                ('lastname', models.TextField()),
                ('email', models.TextField()),
                ('location', models.TextField()),
                ('category', models.IntegerField(choices=[('Reception', ((11, 'Réceptionniste'), (12, 'Chef de réception'))), ('Salle', ((21, "Maître d'hôtel"), (22, 'Serveur(se)'), (23, 'Sommelier'), (24, 'Barman'))), ('Entretien', ((31, 'Femme de chambre'), (32, 'Maçon'), (33, 'Plombier'), (34, 'Electricien'))), ('Restauration', ((41, 'Cuisinier'), (42, 'Chef de cuisine'), (43, 'Patissier'))), ('Sécurité', ((51, 'Agent de sécurité'), (52, 'Chef de sécurité'), (53, 'Spécialiste caméras')))])),
                ('description', models.TextField()),
                ('CV', models.FileField(upload_to='')),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
