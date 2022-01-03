from django.db import transaction
from django.views.generic.base import TemplateView

from ICM.models import Magazin


class MagazinePageView(TemplateView):
    template_name = "magazine.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with transaction.atomic():
            magazine = Magazin.objects.all()
        context['magazine'] = magazine
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('updateMagazin', None) is not None:
            with transaction.atomic():
                magazin = Magazin.objects.get(idmagazin=int(self.request.POST.get('Select_magazin_Update', None)))

            nume_magazin = self.request.POST.get('NUME_MAGAZIN_update', None)
            telefon = self.request.POST.get('TELEFON_update', None)
            email = self.request.POST.get('EMAIL_update', None)
            oras = self.request.POST.get('ORAS_update', None)
            adresa = self.request.POST.get('ADRESA_update', None)
            codpostal = self.request.POST.get('CODPOSTAL_update', None)

            nume_magazin = nume_magazin if nume_magazin != '' else magazin.nume_magazin
            telefon = telefon if telefon != '' else magazin.telefon
            email = email if email != '' else magazin.email
            oras = oras if oras != '' else magazin.oras
            adresa = adresa if adresa != '' else magazin.adresa
            codpostal = codpostal if codpostal != '' else magazin.codpostal

            magazin = Magazin(idmagazin=magazin.idmagazin, nume_magazin=nume_magazin, telefon=telefon, email=email,
                              oras=oras, adresa=adresa, codpostal=codpostal)
            magazin.update_magazin()

        elif self.request.POST.get('deleteMagazin', None) is not None:
            with transaction.atomic():
                magazin = Magazin.objects.get(idmagazin=int(self.request.POST.get('Select_Magazin_Delete', None)))
            magazin.delete_magazin()

        return self.render_to_response(self.get_context_data())
