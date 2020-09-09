# myapp/api.py
from tastypie.resources import ModelResource
from polls.models import SateliteTelemetry


class EntryResource(ModelResource):
    class Meta:
        queryset = SateliteTelemetry.objects.all()
        resource_name = 'Satelite_Telemetry'
