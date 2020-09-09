from polls.models import SateliteTelemetry
from polls.scripts.Reciver import Reciver


class DataArrays:
    data_reciver=Reciver()
    cont=0

    @classmethod
    def populate(cls, line):
        cls.cont=cls.cont + 1
        if cls.cont == 1:
            cls.data_reciver.blankPack()

        cls.data_reciver.generatePackage(line)
        msg1=cls.data_reciver.contador_mensagens1
        msg2=cls.data_reciver.contador_mensagens2
        msg3=cls.data_reciver.contador_mensagens3

        print(msg1)
        print(msg2)
        print(msg3)

        if msg1 is not None and msg2 is not None and msg3 is not None:
            if msg1 == msg2 == msg3:
                p=SateliteTelemetry()
                p.sync=cls.data_reciver.sync

                p.contador_mensagens=cls.data_reciver.contador_mensagens3
                p.nro_pacote1=cls.data_reciver.nro_pacote1

                p.nro_pacote2=cls.data_reciver.nro_pacote2
                p.nro_pacote3=cls.data_reciver.nro_pacote3
                p.latitude_gps=cls.data_reciver.latitude_gps
                p.longitude_gps=cls.data_reciver.longitude_gps
                p.dia=cls.data_reciver.dia
                p.mes=cls.data_reciver.mes
                p.ano=cls.data_reciver.ano
                p.hora=cls.data_reciver.hora
                p.minuto=cls.data_reciver.minuto
                p.segundo=cls.data_reciver.segundo
                p.hdop=cls.data_reciver.hdop
                p.nro_satelite=cls.data_reciver.nro_satelite
                p.speed=cls.data_reciver.speed
                p.curso=cls.data_reciver.curso
                p.altitude_gps=cls.data_reciver.altitude_gps
                p.pot_rec_bal=cls.data_reciver.pot_rec_bal
                p.temp_inter_um=cls.data_reciver.temp_inter_um
                p.temp_ext=cls.data_reciver.temp_ext
                p.temp_inter_dois=cls.data_reciver.temp_inter_dois

                p.pressao=cls.data_reciver.pressao
                p.pressao_mar=cls.data_reciver.pressao_mar
                p.altitude_BMP=cls.data_reciver.altitude_BMP
                p.pot_tx_no_balao=cls.data_reciver.pot_tx_no_balao
                p.status_header=cls.data_reciver.status_header
                p.status_temperatura=cls.data_reciver.status_temperatura
                p.ds18b20=cls.data_reciver.ds18b20
                p.bmp180=cls.data_reciver.bmp180
                p.sdcard=cls.data_reciver.sdcard
                p.gpsPresent=cls.data_reciver.gpsPresent
                p.potenc_est=cls.data_reciver.potenc_est

                p.save()

                cls.cont = 0


