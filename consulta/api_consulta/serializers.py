from rest_framework import serializers
from consulta.models import Consultas
from equipe.models import Medicos, Agenda, Especialidades
from rest_framework.serializers import ModelSerializer, SlugRelatedField, StringRelatedField, HyperlinkedIdentityField, ValidationError
from equipe.api_equipe.serializers import MedicosSerializer

class ConsultasSerializer(serializers.ModelSerializer):
    dia = serializers.CharField(read_only=True, source="agenda.dia")
    horario = serializers.CharField(read_only=True, source="agenda.horarios")
    medico = MedicosSerializer(source="agenda.medico", many=False)
    class Meta:
        model = Consultas
        fields = ['dia','horario','data_agendamento','medico']