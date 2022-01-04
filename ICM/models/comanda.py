from django.db import models
from django.db import transaction

from ICM.models import Client, Magazin


class Comanda(models.Model):
    status_comanda_choices = [
        ('Anulată', 'Anulată'),
        ('Livrată', 'Livrată'),
        ('În așteptare', 'În așteptare'),
        ('Returnată', 'Returnată'),
    ]

    idcomanda = models.BigAutoField(db_column='IDCOMANDA', primary_key=True)  # Field name made lowercase.
    status_comanda = models.CharField(db_column='STATUS_COMANDA', max_length=45,
                                      choices=status_comanda_choices)  # Field name made lowercase.
    data_plasarii = models.DateField(db_column='DATA_PLASARII')  # Field name made lowercase.
    ora_plasarii = models.TimeField(db_column='ORA_PLASARII')  # Field name made lowercase.
    data_livrarii = models.DateField(db_column='DATA_LIVRARII', blank=True, null=True)  # Field name made lowercase.
    ora_livrarii = models.TimeField(db_column='ORA_LIVRARII', blank=True, null=True)  # Field name made lowercase.
    client = models.ForeignKey(Client, models.CASCADE, db_column='IDCLIENT')  # Field name made lowercase.
    magazin = models.ForeignKey(Magazin, models.CASCADE, db_column='IDMAGAZIN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comenzi'
        verbose_name = 'Comandă'
        verbose_name_plural = 'Comenzi'
        ordering = ['status_comanda', 'data_plasarii', 'ora_plasarii']

    def __str__(self):
        return self.represent

    @property
    def represent(self):
        return F"{self.data_plasarii} {self.ora_plasarii} - {self.client.nume_client} ({self.client.cnp})"

    def new_comanda(self):
        with transaction.atomic():
            self.save(force_insert=True)

    def update_comanda(self):
        with transaction.atomic():
            self.save(force_update=True)

    def delete_comanda(self):
        with transaction.atomic():
            self.delete()
