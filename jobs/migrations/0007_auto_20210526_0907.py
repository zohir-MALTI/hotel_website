# Generated by Django 3.0 on 2021-05-26 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0006_auto_20210519_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='cv_file',
            field=models.FileField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='picture',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_date', models.DateTimeField(auto_now_add=True)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
