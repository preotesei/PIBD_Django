from django.db import transaction
from django.views.generic.base import TemplateView

from ICM.models import Client


class ClientiPageView(TemplateView):
    template_name = "clienti.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with transaction.atomic():
            clienti = Client.objects.all()
        context['clienti'] = clienti
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('updateClient', None) is not None:
            with transaction.atomic():
                client = Client.objects.get(idclient=int(self.request.POST.get('Select_client_Update', None)))

            cnp = self.request.POST.get('CNP_update', None)
            nume = self.request.POST.get('Nume_update', None)
            prenume = self.request.POST.get('Prenume_update', None)
            telefon = self.request.POST.get('Telefon_update', None)
            email = self.request.POST.get('Email_update', None)
            oras = self.request.POST.get('oras_update', None)
            adresa = self.request.POST.get('adresa_update', None)
            codpostal = self.request.POST.get('cod_postal_update', None)

            cnp = cnp if cnp != '' else client.cnp
            nume = nume if nume != '' else client.nume
            prenume = prenume if prenume != '' else client.prenume
            telefon = telefon if telefon != '' else client.telefon
            email = email if email != '' else client.email
            oras = oras if oras != '' else client.oras
            adresa = adresa if adresa != '' else client.adresa
            codpostal = codpostal if codpostal != '' else client.codpostal

            client = Client(idclient=client.idclient, cnp=cnp, nume=nume, prenume=prenume, telefon=telefon, email=email,
                            oras=oras, adresa=adresa, codpostal=codpostal)
            client.update_client()

        elif self.request.POST.get('deleteClient', None) is not None:

            with transaction.atomic():
                client = Client.objects.get(idclient=int(self.request.POST.get('Select_client_Delete', None)))

            client.delete_client()

        return self.render_to_response(self.get_context_data())

