class Reciver:
    # Sync
    sync = None

    # Cabecalhos

    contador_mensagens1 = None
    contador_mensagens2 = None
    contador_mensagens3 = None
    nro_pacote1 = None
    nro_pacote2 = None
    nro_pacote3 = None

    # Pacote1
    latitude_gps = None
    longitude_gps = None
    dia = None
    mes = None
    ano = None
    hora = None
    minuto = None
    segundo = None

    # Pacote2
    hdop = None
    nro_satelite = None
    speed = None
    curso = None
    altitude_gps = None
    pot_rec_bal = None
    temp_inter_um = None
    temp_ext = None
    temp_inter_dois = None

    # Pacote3
    pressao = None
    pressao_mar = None
    altitude_BMP = None
    pot_tx_no_balao = None
    status_header = None
    status_temperatura = None
    ds18b20 = None
    bmp180 = None
    sdcard = None
    gpsPresent = None
    potenc_est = None

    # Separador
    separador = None
    separador2 = None

    def blankPack(self):
        # Sync
        self.sync = None

        # Cabecalhos
        self.contador_mensagens1 = None
        self.contador_mensagens2 = None
        self.contador_mensagens3 = None
        self.nro_pacote1 = None
        self.nro_pacote2 = None
        self.nro_pacote3 = None

        # Pacote1
        self.latitude_gps = None
        self.longitude_gps = None
        self.dia = None
        self.mes = None
        self.ano = None
        self.hora = None
        self.minuto = None
        self.segundo = None

        # Pacote2
        self.hdop = None
        self.nro_satelite = None
        self.speed = None
        self.curso = None
        self.altitude_gps = None
        self.pot_rec_bal = None
        self.temp_inter_um = None
        self.temp_ext = None
        self.temp_inter_dois = None

        # Pacote3
        self.pressao = None
        self.pressao_mar = None
        self.altitude_BMP = None
        self.pot_tx_no_balao = None
        self.status_header = None
        self.status_temperatura = None
        self.ds18b20 = None
        self.bmp180 = None
        self.sdcard = None
        self.gpsPresent = None
        self.potenc_est = None

        # Separador
        self.separador = None
        self.separador2 = None

    def generatePackage(self, dados):
        arr = dados.split(' ')
        if arr[0] == "EB90":
            self.blankPack()
            self.sync = arr[0]
            self.contador_mensagens1 = int(arr[1])
            self.nro_pacote1 = int(arr[2])

            self.pacote_um(arr)

        else:
            if self.nro_pacote1 is not None:
                nro_pacote = int(arr[1])
                if nro_pacote == 2:
                    self.contador_mensagens2 = int(arr[0])
                    self.nro_pacote2 = nro_pacote
                    self.pacote_dois(arr)
                else:
                    self.contador_mensagens3 = int(arr[0])
                    self.nro_pacote3 = nro_pacote
                    self.pacote_tres(arr)

    def pacote_um(self, arr):
        self.latitude_gps = float(arr[3])
        self.longitude_gps = float(arr[4])
        self.dia = int(arr[5])
        self.mes = int(arr[6])
        self.ano = int(arr[7])
        self.hora = int(arr[8])
        self.minuto = int(arr[9])
        self.segundo = int(arr[10])
        self.separador = arr[11]

    def pacote_dois(self, arr):
        self.hdop = int(arr[2])
        self.nro_satelite = int(arr[3])
        self.speed = float(arr[4])
        self.curso = float(arr[5])
        self.altitude_gps = int(arr[6])
        self.pot_rec_bal = int(arr[7])

        self.temp_inter_um = float(arr[8])
        self.temp_ext = float(arr[9])
        self.temp_inter_dois = float(arr[10])
        self.separador = arr[11]

    def pacote_tres(self, arr):
        self.pressao = float(arr[2])
        self.pressao_mar = float(arr[3])
        self.altitude_BMP = float(arr[4])
        self.pot_tx_no_balao = float(arr[5])
        self.status_header = int(arr[6])
        self.status_temperatura = int(arr[7])
        self.ds18b20 = int(arr[8])
        self.bmp180 = int(arr[9])
        self.sdcard = int(arr[10])
        self.gpsPresent = int(arr[11])
        self.separador = arr[12]
        self.potenc_est = int(arr[13])
        self.separador2 = arr[14]

    def validPack(self):
        return not((self.nro_pacote1 is None and self.nro_pacote2 is None) and self.nro_pacote3 is None)
