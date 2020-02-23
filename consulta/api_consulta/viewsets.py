from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from consulta.models import Consultas
from consulta.api_consulta.serializers import ConsultasSerializer
from rest_framework import filters



class ConsultasViewset(viewsets.ModelViewSet):
    queryset = Consultas.objects.all()
    serializer_class = ConsultasSerializer
