from serial import Serial, unicode
import time
from polls.scripts.DataArrays import DataArrays

from polls.models import SateliteMensagem


def run():
    print("INIT")
    ser=Serial('COM8', 9600, timeout=3)
    time.sleep(3)
    print("Serial is open: " + str(ser.isOpen()))
    array = DataArrays()
    loc="null"
    while (True):

        for msg in SateliteMensagem.objects.order_by("-id")[:1]:
            if not(msg.enviado):
                print(msg.criacao)
                print(msg.update)
                print(msg.datalog)
                loc2 = "D"+msg.datalog+"\n"
                ser.flushInput()
                print(loc2)
                msg.enviado = True
                msg.save()
                print(msg.enviado)
                ser.write(loc2.encode())
                loc = msg.enviado


        ser.flushOutput()
        line=ser.readline()
        print("line" + line.decode("utf-8"))
        print(loc)

        if line.decode("utf-8") and loc == line.decode("utf-8"):

            lineForm = line.decode("utf-8")
            print(lineForm)
            array.populate(lineForm)

