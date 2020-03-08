from rest_framework import viewsets, status, filters
from consulta.models import Consulta
from equipe.models import Agenda
from consulta.api_consulta.serializers import ConsultaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAdminUser
from datetime import date
from datetime import datetime
from django.shortcuts import get_object_or_404


def horarios_passados():
    agendas = Agenda.objects.filter(dia=date.today())
    for agenda in agendas:
        for marcados in agenda.horarios.all():
            if marcados.horario < f'{datetime.today().hour}:{datetime.today().minute}':
                agenda.horarios.remove(marcados.id)
    return


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class ConsultaViewset(viewsets.ModelViewSet):
    authentication_classes = ['TokenAuthentication']
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    authentication_classes = [CsrfExemptSessionAuthentication]
    serializer_class = ConsultaSerializer
    filterset_fields = ['data_agendamento', 'id']

    def list(self, request):
        horarios_passados()
        self.queryset = Consulta.objects.all()
        serializer = ConsultaSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        agenda = Agenda.objects.filter(id=request.data['agenda_id'])[0]
        paciente = request.user
        horario = request.data['horario']
        consultas = Consulta(paciente=paciente, agenda=agenda, horario=horario)
        if consultas.clean():
            return
        else:
            consultas = Consulta.objects.create(
                paciente=paciente, agenda=agenda, horario=horario)
            agenda = Agenda.objects.filter(
                medico=agenda.medico, dia=agenda.dia)[0]
            horario = agenda.horarios.filter(horario=horario)[0].id
            horarios = agenda.horarios
            horarios.remove(horario)
            queryset = Consulta.objects.filter(id=consultas.id)
            serializer = ConsultaSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        self.queryset = Consulta.objects.all()
        consulta = get_object_or_404(self.queryset, pk=pk)
        if request.user == consulta.paciente:
            consulta.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
