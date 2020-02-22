from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from equipe.models import Especialidades, Medicos
from equipe.api_equipe.serializers import EspecialidadesSerializer, MedicosSerializer
from rest_framework import filters



class MedicosViewset(viewsets.ModelViewSet):
    queryset = Medicos.objects.all()
    serializer_class = MedicosSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nome']
    filterset_fields = ['especialidade']

class EspecialidadesViewSet(viewsets.ModelViewSet):
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']