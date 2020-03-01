from django.db.models import Q
from django.utils import timezone
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from equipe.models import Especialidades, Medicos, Agenda
from equipe.api_equipe.serializers import EspecialidadesSerializer, MedicosSerializer, AgendaSerializer
from rest_framework import filters


class MedicosViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Medicos.objects.all()
    serializer_class = MedicosSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nome']
    filterset_fields = ['especialidade']

class EspecialidadesViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']

class AgendaViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Agenda.objects.filter(dia__gte=timezone.now()).order_by('dia')
    serializer_class = AgendaSerializer
    filter_backends = [filters.SearchFilter]