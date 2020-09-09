from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse

from django.http import HttpResponse

from .form import PostForm
from .models import SateliteTelemetry, AntenaPositions, SateliteMensagem
from .scripts.bp import Controle


def index(request):
    template=loader.get_template('polls/index.html')
    context={}
    return HttpResponse(template.render(context, request))


def polls_list(request):
    MAX_OBJECTS=5
    satelite_telemetry=SateliteTelemetry.objects.order_by("-id")[:MAX_OBJECTS]
    data={"results1": list(satelite_telemetry.values())}
    estacao = AntenaPositions.objects.order_by("-id")[:1]
    data2 = {"results2":list(estacao.values())}
    print(data2)

    arrSat = [satelite_telemetry[0].latitude_gps,satelite_telemetry[0].longitude_gps,satelite_telemetry[0].altitude_gps]
    arrAntena = [estacao[0].latitude_antena,estacao[0].longitude_antena,estacao[0].altitude_ant]
    print(arrAntena)
    print(arrSat)
    bp = Controle()
    result = bp.balloon_gps_receiver_pointing(arrSat,arrAntena)
    resultToFloat = [float(result[0]),float(result[1]),float(result[2])]

    print(resultToFloat)
    data3 = {"results3":list(resultToFloat)}
    print(data2)

    cont=len(data["results1"])
    for x in range(0, cont):
        print(x)
        if data["results1"][x]["status_header"] == 0:
            data["results1"][x]["status_header"]="Desabilitado"
        else:
            data["results1"][x]["status_header"]="Habilitado"

        if data["results1"][x]["status_temperatura"] == 0:
            data["results1"][x]["status_temperatura"]="Desabilitado"
        else:
            data["results1"][x]["status_temperatura"]="Habilitado"

        if data["results1"][x]["ds18b20"] == 0:
            data["results1"][x]["ds18b20"]="Ausente"
        else:
            data["results1"][x]["ds18b20"]="Presente"

        if data["results1"][x]["bmp180"] == 0:
            data["results1"][x]["bmp180"]="Ausente"
        else:
            data["results1"][x]["bmp180"]="Presente"

        if data["results1"][x]["sdcard"] == 0:
            data["results1"][x]["sdcard"]="Ausente"
        else:
            data["results1"][x]["sdcard"]="Presente"

        if data["results1"][x]["gpsPresent"] == 0:
            data["results1"][x]["gpsPresent"]="Ausente"
        else:
            data["results1"][x]["gpsPresent"]="Presente"

    data4 = dict(list(data.items()) + list(data2.items())+ list(data3.items()))

    return JsonResponse(data4)


def polls_detail(request, pk):
    pass


def maps(request):
    template=loader.get_template('polls/maps.html')
    context={}
    return HttpResponse(template.render(context, request))

def telecomando(request):
    form = PostForm()
    if request.method == "POST":
        x = request.POST.copy()
        print(x)
        form.process(x)

    return render(request, 'polls/telecomando.html', {'form': form},)

