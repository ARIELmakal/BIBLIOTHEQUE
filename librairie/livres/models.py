from django.db import models

# Create your models here.
class Livres(models.Model):
    livre = models.CharField(max_length= 50)
    Auteur = models.CharField(max_length= 58)
    Description = models.TextField()
    actif = models.BooleanField()
    image = models.ImageField(upload_to='images', blank = True)

    class Meta:
        verbose_name = ("Livre")
        verbose_name_plural = ("Livres")

    def __str__(self):
        return self.livre

class Messages(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name = ("Message")
        verbose_name_plural = ("Messages")

    def __str__(self):
        return self.nom
