from django.db import models

# Create your models here.
class Oddeleni(models.Model):
    code = models.CharField(max_length=3)
    nazev = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nazev} ({self.code})"
    
class Pokoje(models.Model):
    Oddeleni = models.ForeignKey(Oddeleni, on_delete=models.PROTECT, related_name="pacienti")
    Cislo = models.IntegerField()

    def __str__(self):
        return f"{self.id}: -> {self.Oddeleni} ({self.Cislo})"

class Pacient(models.Model):
    First = models.CharField(max_length=64)
    Last = models.CharField(max_length=64)
    Oddeleni = models.ManyToManyField(Pokoje, blank=True, related_name="pokoje")

    def __str__(self):
        return f"{self.first} {self.last} -> {self.Oddeleni} "    