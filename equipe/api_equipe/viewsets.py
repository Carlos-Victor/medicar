from django.utils import timezone
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from equipe.models import Especialidade, Medico, Agenda
from equipe.api_equipe.serializers import EspecialidadeSerializer, MedicoSerializer, AgendaSerializer
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser


class MedicoViewset(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome']
    filterset_fields = ['especialidade']

class EspecialidadeViewset(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']

class AgendaViewset(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Agenda.objects.filter(dia__gte=timezone.now()).order_by('dia')
    serializer_class = AgendaSerializer
    filter_backends = [filters.SearchFilter]
