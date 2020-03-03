from rest_framework import viewsets
from consulta.models import Consultas
from consulta.api_consulta.serializers import ConsultasSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ConsultasViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Consultas.objects.all()
    serializer_class = ConsultasSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['data_agendamento','id']