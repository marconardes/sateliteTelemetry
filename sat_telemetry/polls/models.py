from django.db import models
import datetime

# Create your models here.
from django.db import models


class SateliteTelemetry(models.Model):
    sync=models.CharField(max_length=5)
    contador_mensagens=models.PositiveIntegerField()
    nro_pacote1=models.IntegerField()
    nro_pacote2=models.IntegerField()
    nro_pacote3=models.IntegerField()

    # Pacote1
    latitude_gps=models.FloatField()
    longitude_gps=models.FloatField()
    dia=models.IntegerField()
    mes=models.IntegerField()
    ano=models.IntegerField()
    hora=models.IntegerField()
    minuto=models.IntegerField()
    segundo=models.IntegerField()

    # Pacote2
    hdop=models.IntegerField()
    nro_satelite=models.IntegerField()
    speed=models.FloatField()
    curso=models.FloatField()
    altitude_gps=models.FloatField()
    pot_rec_bal=models.FloatField()
    temp_inter_um=models.FloatField()
    temp_ext=models.FloatField()
    temp_inter_dois=models.FloatField()

    # Pacote3
    pressao=models.FloatField()
    pressao_mar=models.FloatField()
    altitude_BMP=models.IntegerField()
    pot_tx_no_balao=models.FloatField()
    status_header=models.IntegerField()
    status_temperatura=models.IntegerField()
    ds18b20=models.IntegerField()
    bmp180=models.IntegerField()
    sdcard=models.IntegerField()
    gpsPresent=models.IntegerField()
    potenc_est=models.IntegerField()


class SateliteLog(models.Model):
    datalog=models.CharField(max_length=200)


class AntenaPositions(models.Model):
    latitude_antena=models.FloatField()
    longitude_antena=models.FloatField()
    altitude_ant=models.FloatField(null=True)


class AntenaMoviment(models.Model):
    distancia=models.FloatField()
    azimute=models.FloatField()
    elevação=models.FloatField()

class SateliteMensagem(models.Model):
    datalog=models.CharField(max_length=60)
    criacao = models.DateTimeField(auto_now_add=True, blank=True)
    update=models.DateTimeField(auto_now_add=False, blank=True)
    enviado = models.BooleanField(default=False)
