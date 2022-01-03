from django.db import models
from django.db import transaction


class Client(models.Model):
    idclient = models.BigAutoField('ID Client', db_column='IDCLIENT', primary_key=True)  # Field name made lowercase.
    cnp = models.CharField('CNP', db_column='CNP', max_length=45)  # Field name made lowercase.
    nume = models.CharField('Nume', db_column='NUME', max_length=45)  # Field name made lowercase.
    prenume = models.CharField('Prenume', db_column='PRENUME', max_length=45)  # Field name made lowercase.
    telefon = models.CharField('Telefon', db_column='TELEFON', max_length=45)  # Field name made lowercase.
    email = models.CharField('Email', db_column='EMAIL', max_length=255)  # Field name made lowercase.
    oras = models.CharField('Oraș', db_column='ORAS', max_length=45)  # Field name made lowercase.
    adresa = models.CharField('Adresă', db_column='ADRESA', max_length=255)  # Field name made lowercase.
    codpostal = models.CharField('Cod Poștal', db_column='CODPOSTAL', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clienti'
        verbose_name = 'Client'
        verbose_name_plural = 'Clienți'
        ordering = ['prenume', 'nume']

    def __str__(self):
        return self.represent

    @property
    def nume_client(self):
        return F"{self.prenume} {self.nume}"

    @property
    def represent(self):
        return F"{self.nume_client} ({self.cnp})"

    def new_client(self):
        with transaction.atomic():
            self.save(force_insert=True)

    def update_client(self):
        with transaction.atomic():
            self.save(force_update=True)

    def delete_client(self):
        with transaction.atomic():
            self.delete()
