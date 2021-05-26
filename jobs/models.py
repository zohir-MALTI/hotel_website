from django.db import models
from django.contrib.auth.models import User

JOBS_CHOICES = [
    ('Reception', (
        (11, 'Réceptionniste'), (12, 'Chef de réception'),
    )),
    ('Salle', (
        (21, 'Maître d\'hôtel'), (22, 'Serveur(se)'), (23, 'Sommelier'), (24, 'Barman'),
    )),
    ('Entretien', (
        (31, 'Femme de chambre'), (32, 'Maçon'), (33, 'Plombier'), (34, 'Electricien'),
    )),
    ('Restauration', (
        (41, 'Cuisinier'), (42, 'Chef de cuisine'), (43, 'Patissier'),
    )),
    ('Sécurité', (
        (51, 'Agent de sécurité'), (52, 'Chef de sécurité'), (53, 'Spécialiste caméras'),
    )),
]

JOBS_TYPES = [
    ('CDI', 'CDI'), ('CDD', 'CDD'), ('SAIS', 'Saisonier'),
]


class Job(models.Model):

    title = models.TextField()
    company = models.TextField()
    location = models.TextField()
    salary = models.TextField()
    link = models.URLField()
    category = models.IntegerField(choices=JOBS_CHOICES)
    contract_type = models.CharField(max_length=4, choices=JOBS_TYPES)
    description = models.TextField(blank=True)
    job_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary_of_description(self):
        desc = self.description
        if len(desc) > 130:
            return desc[:130]+"..."
        return desc


class CV(models.Model):

    picture = models.ImageField(upload_to='media/')
    firstname = models.TextField()
    lastname = models.TextField()
    email = models.TextField()
    location = models.TextField()
    category = models.IntegerField(choices=JOBS_CHOICES)
    description = models.TextField()
    cv_file = models.FileField(upload_to='media/')
    registration_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname + self.lastname.upper()

    def pretty_date(self):
        return self.registration_date.strftime("%d/%m/%Y")


class Likes(models.Model):
    user_id   = models.ForeignKey(User, on_delete=models.CASCADE)
    job_id    = models.ForeignKey(Job,  on_delete=models.CASCADE)
    like_date = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    user_id   = models.ForeignKey(User, on_delete=models.CASCADE)
    job_id    = models.ForeignKey(Job,  on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment  = models.TextField()

    def pretty_date(self):
        return self.comment_date.strftime("%Y-%m-%d %H:%M")


class Applications(models.Model):
    user_id   = models.ForeignKey(User, on_delete=models.CASCADE)
    job_id    = models.ForeignKey(Job,  on_delete=models.CASCADE)
    app_date = models.DateTimeField(auto_now_add=True)

