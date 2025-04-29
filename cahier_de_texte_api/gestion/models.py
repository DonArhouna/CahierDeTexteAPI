from django.db import models
from django.contrib.auth.models import AbstractUser


class Campus(models.Model):
    nom = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

class Filiere(models.Model):
    nom = models.CharField(max_length=100)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='filieres')

    def __str__(self):
        return f"{self.nom} ({self.campus.nom})"

class Classe(models.Model):
    nom = models.CharField(max_length=100)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, related_name='classes')

    def __str__(self):
        return f"{self.nom} ({self.filiere.nom})"

class Cours(models.Model):
    nom = models.CharField(max_length=100)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='cours')

    def __str__(self):
        return f"{self.nom} ({self.classe.nom})"

class Professeur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    matricule = models.CharField(max_length=50, unique=True)
    cours = models.ManyToManyField(Cours, related_name='professeurs')

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Responsable(models.Model):
    nom = models.CharField(max_length=100, null=True, blank=True)
    prenom = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    matricule = models.CharField(max_length=50, unique=True, null=True, blank=True)
    campus = models.ForeignKey('Campus', on_delete=models.CASCADE, related_name='responsables', null=True, blank=True)
    filieres = models.ManyToManyField('Filiere', related_name='responsables', blank=True)


    # Ajoute des related_name personnalisés pour éviter les conflits
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="responsable_groups",  # Nom personnalisé
        related_query_name="responsable",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="responsable_user_permissions",  # Nom personnalisé
        related_query_name="responsable",
    )

    def __str__(self):
        return self.username

""" class Responsable(AbstractUser):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='responsables', null=True, blank=True)
    filieres = models.ManyToManyField(Filiere, related_name='responsables', blank=True)

    def __str__(self):
        return self.username """

class Emargement(models.Model):
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE, related_name='emargements')
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='emargements')

    def __str__(self):
        return f"{self.date} - {self.cours.nom}"

class CahierDeTexte(models.Model):
    date = models.DateField()
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='cahiers_de_texte')
    parties_traitees = models.TextField()

    def __str__(self):
        return f"{self.date} - {self.cours.nom}"