from rest_framework import viewsets, status, filters
from consulta.models import Consultas
from equipe.models import Agenda
from consulta.api_consulta.serializers import ConsultasSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
import json
from django.http import JsonResponse

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class ConsultasViewset(viewsets.ModelViewSet):
    queryset = Consultas.objects.all()
    serializer_class = ConsultasSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['data_agendamento','id']
    authentication_classes = [CsrfExemptSessionAuthentication]

    def create(self, request):
        if request.method == 'POST':
            agenda = Agenda.objects.filter(id=request.data['agenda_id'])[0]
            paciente = request.user
            horario = request.data['horario']
            consultas = Consultas(
                paciente=paciente,
                agenda=agenda,
                horario=horario
            )
            if consultas.clean():
                return 
            else:
                consultas.save()
                agenda = Agenda.objects.filter(medico=agenda.medico,dia=agenda.dia)[0]
                horario = agenda.horarios.filter(horario=horario)[0].id
                horarios = agenda.horarios
                horarios.remove(horario)
                return Response(status=status.HTTP_201_CREATED)

                