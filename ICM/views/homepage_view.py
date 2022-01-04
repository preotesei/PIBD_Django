from dateutil.parser import parse
from django.db import transaction
from django.views.generic.base import TemplateView

from ICM.models import Client, Magazin, Comanda


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with transaction.atomic():
            clienti = Client.objects.all()
            magazine = Magazin.objects.all()
        context['clienti'] = clienti
        context['magazine'] = magazine
        return context

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('addClient', None) is not None:
            client = Client()
            client.cnp = self.request.POST.get('cnp_add', None)
            client.nume = self.request.POST.get('nume_add', None)
            client.prenume = self.request.POST.get('prenume_add', None)
            client.telefon = self.request.POST.get('telefon_add', None)
            client.email = self.request.POST.get('email_add', None)
            client.oras = self.request.POST.get('oras_add', None)
            client.adresa = self.request.POST.get('adresa_add', None)
            client.codpostal = self.request.POST.get('cod_postal_add', None)
            client.new_client()

        elif self.request.POST.get('addMagazin', None) is not None:
            magazin = Magazin()
            magazin.nume_magazin = self.request.POST.get('NUME_MAGAZIN_add', None)
            magazin.telefon = self.request.POST.get('TELEFON_MAGAZIN_add', None)
            magazin.email = self.request.POST.get('EMAIL_MAGAZIN_add', None)
            magazin.oras = self.request.POST.get('ORAS_MAGAZIN_add', None)
            magazin.adresa = self.request.POST.get('ADRESA_MAGAZIN_add', None)
            magazin.codpostal = self.request.POST.get('COD_POSTAL_MAGAZIN_add', None)
            magazin.new_magazin()

        elif self.request.POST.get('addComanda', None) is not None:

            with transaction.atomic():
                client = Client.objects.get(idclient=int(self.request.POST.get('IDCLIENT_add', None)))
                magazin = Magazin.objects.get(idmagazin=int(self.request.POST.get('IDMAGAZIN_add', None)))

            comanda = Comanda()
            comanda.client = client
            comanda.magazin = magazin
            comanda.status_comanda = self.request.POST.get('STATUS_COMANDA_add', None)
            comanda.data_plasarii = self.request.POST.get('DATA_PLASARII_add', None)
            comanda.ora_plasarii = self.request.POST.get('ORA_PLASARII_add', None)


            data_livrarii_string = self.request.POST.get('DATA_LIVRARII_add', None)
            ora_livrarii_string = self.request.POST.get('ORA_LIVRARII_add', None)

            comanda.data_livrarii = parse(data_livrarii_string) if data_livrarii_string != '' else None
            comanda.ora_livrarii = parse(ora_livrarii_string) if ora_livrarii_string != '' else None


            # if data_livrarii_string != '':
            #     comanda.data_livrarii = parse(data_livrarii_string)
            # else:
            #     comanda.data_livrarii = None

            # if ora_livrarii_string != '':
            #     comanda.ora_livrarii = parse(ora_livrarii_string)

            # comanda.data_livrarii = parse(self.request.POST.get('DATA_LIVRARII_add', None))
            # comanda.ora_livrarii = parse(self.request.POST.get('ORA_LIVRARII_add', None))

            comanda.new_comanda()

        return self.render_to_response(self.get_context_data())
