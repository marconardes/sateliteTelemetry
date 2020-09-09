from decimal import Decimal

from django import forms

from .models import SateliteMensagem
from datetime import datetime


class PostForm(forms.Form):
        controle_de_temperatura=forms.BooleanField(required=False)
        temperatura_minima=forms.DecimalField(initial=27.0, min_value=-10.0, max_value=100.0,decimal_places = 1 )
        temperatura_maxima=forms.DecimalField(initial=28.0, min_value=-10.0, max_value=100.0,decimal_places = 1 )
        CHOICES=(('20', '20'), ('14', '14'),('12', '12'), ('10', '10'),('08', '08'),('06', '06'),('04', '04'),('02', '02'),('00', '00'),('-2', '-2'),)
        ligar_potencia_TX=forms.BooleanField(required=False)

        potencia_TX = forms.ChoiceField(choices=CHOICES)

        def process(self, request):
            print(request)
            print(request.get("controle_de_temperatura"))
            self.controle_de_temperatura = request.get("controle_de_temperatura")
            self.temperatura_minima=request.get("temperatura_minima")
            self.temperatura_maxima=request.get("temperatura_maxima")
            self.potencia_TX=request.get("potencia_TX")
            self.ligar_potencia_TX = request.get("ligar_potencia_TX")

            dados="EB90 1 "
            if( self.controle_de_temperatura =='on'):
                dados = dados +"1 "
            else:
                dados = dados + "0 "

            temperatura_minimaLoc = str(self.temperatura_minima).zfill(5)
            temperatura_maximaLoc = str(self.temperatura_maxima).zfill(5)

            print(temperatura_minimaLoc)
            print(temperatura_maximaLoc)
            dados = dados + temperatura_minimaLoc+" "+temperatura_maximaLoc
            if (self.ligar_potencia_TX == 'on'):
                dados=dados + " 1 "
            else:
                dados=dados + " 0 "

            dados = dados + str(self.potencia_TX) +" 0"
            print(dados)
            sm = SateliteMensagem()
            sm.datalog = dados
            sm.update = datetime.now()
            sm.save()