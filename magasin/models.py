from unittest.util import _MAX_LENGTH
from django.db import models


class Article(models.Model) :
    libelle = models.CharField(max_length=25)
    prix = models.FloatField()
    qte = models.IntegerField()
    dateAjout = models.DateField()
    categ = models.ForeignKey('Categorie', on_delete=models.CASCADE,)


def __str__(self) -> str:
 return self.libelle
#     a1 = Article(libelle='Lait',prix=1.4, qte=48,dateAjout='2022-10-01')
#     a2 = Article (libelle='Champoing', prix=9.870, qte=11, dateAjout= '2022-10-01')
#     a3 = Article(libelle='Huile', prix=32.130, qte=3, dateAjout='2022-10-03')
#     liste = [a1, a2, a3]
#     for a in liste :
# a.save()

class Categorie(models.Model) :
   nomCat = models.TextField()
   description = models.TextField()
   def __str__(self) -> str:
    return self.nomCat