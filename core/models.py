from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import User
import os


# Create your models here.


# creation de la classe Classe

class Classe(models.Model):
    niveau = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.niveau


# creation de la classe Matiere

class Matiere(models.Model):
    intitule = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.intitule


# creation la classe Utilisateur

def renommer_image(instance, filename):
    upload_to = 'image/'
    ext = filename.split('.')[-1]
    if instance.user.username:
        filename = "photo_profile/{}.{}".format(instance.user.username, ext)
        return os.path.join(upload_to, filename)


class Utilisateur(models.Model):
    CIVILITE = [
        ('Monsieur', 'Monsieur'), ('Mademoiselle', 'Mademoiselle'), ('Madame', 'Madame')
    ]
    Langue = [
        ('Francais', 'Francais'), ('Anglais', 'Anglais'), ('Billingue', 'Billingue')
    ]
    civilite = models.CharField(max_length=200, null=True, choices=CIVILITE, default='Monsieur')
    langue = models.CharField(max_length=20, null=False, choices=Langue, default='Francais')
    age = models.IntegerField(null=True)
    # User possede déja : username, email, first_name, last_name, (password 1 et 2)
    user = models.OneToOneField(User, on_delete=CASCADE)

    nom = models.CharField(max_length=100, null=False)
    prenom = models.CharField(max_length=100, null=False)
    telephone = models.CharField(max_length=200, null=True)
    photoProfil = models.ImageField(upload_to=renommer_image, blank=True)

    TYPE_USER = [
        ('Élève', 'Élève'), ('Parent', 'Parent'), ('Enseignant', 'Enseignant')
    ]
    type_user = models.CharField(max_length=200, null=True, choices=TYPE_USER, default='Élève')

    # s'inscrire sur la platefoerme
    def inscrire(self):
        pass

    # se connecter à son compte
    def connecter(self):
        pass

    class Meta:
        abstract = True


# creation de la classe Client(élève/parent d'élève) qui est un Utilisateur

class Client(Utilisateur):
    def __str__(self):
        info = self.civilite + " " + self.user.username
        return info

    # rechercher un Repetiteur
    def rechercher(self, matiere, classe, ville, quartier):
        pass

    # consulter le profil d'un Repetiteur
    def consulterProfil(self, repetiteur):
        pass


# creation de la classe Repetiteur qui est un Utilisateur

class Repetiteur(Utilisateur):
    niveauEtude = models.CharField(max_length=200, null=True)
    ville = models.CharField(max_length=200, null=True)
    quartier = models.CharField(max_length=200, null=True)

    def __str__(self):
        info = self.civilite + " " + self.prenom + " " + self.nom
        return info

    # s'inscrire : redefinir la methdode inscrire() de Utilisateur
    def inscrire(self):
        pass

    # modifier son profil (deja inscrit)
    def modifierProfil(self):
        pass


# creation de la classe cours

class Cours(models.Model):
    JOURS = [
        ('lundi', 'lundi'), ('mardi', 'mardi'), ('mercredi', 'mercredi'), ('jeudi', 'jeudi'),
        ('vendredi', 'vendredi'), ('samedi', 'samedi'), ('dimanche', 'dimanche')
    ]
    jour = models.CharField(max_length=200, null=True, choices=JOURS, default='lundi')

    HEURES_DEBUT = [
        ('7H', '7H'), ('8H', '8H'), ('9H', '9H'), ('10H', '10H'), ('11H', '11H'), ('12H', '12H'), ('13H', '13H'),
        ('14H', '14H'), ('15H', '15H'), ('16H', '16H'), ('17H', '17H'), ('18H', '18H')
    ]
    heure_debut = models.CharField(max_length=200, null=True, choices=HEURES_DEBUT, default='7H')

    DUREE = [
        ('1H', '1H'), ('1H30', '1H30'), ('2H', '2H'), ('2H30', '2H30'), ('3H', '3H')
    ]
    duree = models.CharField(max_length=200, null=True, choices=DUREE, default='2H')

    # un Cours a une seulle Matiere
    matiere = models.ForeignKey(Matiere, null=True, on_delete=models.CASCADE)

    # un Cours concerne une seule Classe
    classe = models.ForeignKey(Classe, null=True, on_delete=models.SET_NULL)

    # un Cours est dispensé par un seul Repetiteur
    repetiteur = models.ForeignKey(Repetiteur, null=True, on_delete=models.CASCADE)

    def __str__(self):
        info = self.matiere.intitule + " " + self.classe.niveau
        return info
