from rest_framework import viewsets
from consulta.models import Consultas
from consulta.api_consulta.serializers import ConsultasSerializer



class ConsultasViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Consultas.objects.all()
    serializer_class = ConsultasSerializer
