from django.db import models
from django.db import transaction


class Magazin(models.Model):
    idmagazin = models.BigAutoField('ID Magazin', db_column='IDMAGAZIN', primary_key=True)  # Field name made lowercase.
    nume_magazin = models.CharField('Nume Magazin', db_column='NUME_MAGAZIN',
                                    max_length=45)  # Field name made lowercase.
    telefon = models.CharField('Telefon', db_column='TELEFON', max_length=45)  # Field name made lowercase.
    email = models.CharField('Email', db_column='EMAIL', max_length=255)  # Field name made lowercase.
    oras = models.CharField('Oraș', db_column='ORAS', max_length=45)  # Field name made lowercase.
    adresa = models.CharField('Adresă', db_column='ADRESA', max_length=255)  # Field name made lowercase.
    codpostal = models.CharField('Cod Poștal', db_column='CODPOSTAL', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'magazine'
        verbose_name = 'Magazin'
        verbose_name_plural = 'Magazine'
        ordering = ['oras', 'nume_magazin', 'codpostal']

    def __str__(self):
        return self.represent

    @property
    def represent(self):
        return F"{self.nume_magazin} - {self.oras}"

    def new_magazin(self):
        with transaction.atomic():
            self.save(force_insert=True)

    def update_magazin(self):
        with transaction.atomic():
            self.save(force_update=True)

    def delete_magazin(self):
        with transaction.atomic():
            self.delete()
