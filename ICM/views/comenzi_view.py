from django.db import transaction
from django.views.generic.base import TemplateView
from dateutil.parser import parse

from ICM.models import Comanda


class ComenziPageView(TemplateView):
    template_name = "comenzi.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with transaction.atomic():
            comenzi = Comanda.objects.all()
        context['comenzi'] = comenzi
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('updateComanda', None) is not None:
            with transaction.atomic():
                comanda = Comanda.objects.get(idcomanda=int(self.request.POST.get('Select_comanda_Update')))

            client = comanda.client
            magazin = comanda.magazin
            status_comanda = self.request.POST.get('STATUS_COMANDA_UPDATE', None)
            data_plasarii = self.request.POST.get('DATA_PLASARII_UPDATE', None)
            ora_plasarii = self.request.POST.get('ORA_PLASARII_UPDATE', None)
            # data_livrarii = self.request.POST.get('DATA_LIVRARII_UPDATE', None)
            # ora_livrarii = self.request.POST.get('ORA_LIVRARII_UPDATE', None)

            status_comanda = status_comanda if status_comanda != '' else comanda.status_comanda
            data_plasarii = parse(data_plasarii) if data_plasarii != '' else comanda.data_plasarii
            ora_plasarii = parse(ora_plasarii) if ora_plasarii != '' else comanda.ora_plasarii

            data_livrarii_string = self.request.POST.get('DATA_LIVRARII_UPDATE', None)
            ora_livrarii_string = self.request.POST.get('ORA_LIVRARII_UPDATE', None)

            data_livrarii = parse(data_livrarii_string) if data_livrarii_string != '' else comanda.data_livrarii
            ora_livrarii = parse(ora_livrarii_string) if ora_livrarii_string != '' else comanda.data_livrarii


            # data_livrarii = parse(data_livrarii) if data_livrarii != '' else comanda.data_livrarii
            # ora_livrarii = parse(ora_livrarii) if ora_livrarii != '' else comanda.ora_livrarii

            # data_livrarii = None if data_livrarii != '' else comanda.data_livrarii
            # ora_livrarii = None if ora_livrarii != '' else comanda.ora_livrarii

            comanda = Comanda(idcomanda=comanda.idcomanda, client=client, magazin=magazin,
                              status_comanda=status_comanda, data_plasarii=data_plasarii,
                              ora_plasarii=ora_plasarii, data_livrarii=data_livrarii, ora_livrarii=ora_livrarii)
            comanda.update_comanda()

        elif self.request.POST.get('deleteComanda', None) is not None:
            with transaction.atomic():
                comanda = Comanda.objects.get(idcomanda=int(self.request.POST.get('Select_comanda_Delete', None)))
            comanda.delete_comanda()

        return self.render_to_response(self.get_context_data())
