from rest_framework import serializers
from consulta.models import Consultas
from equipe.models import Medicos, Agenda, Especialidades
from rest_framework.serializers import ModelSerializer, SlugRelatedField, StringRelatedField, HyperlinkedIdentityField, ValidationError




class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidades
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    especialidade = EspecialidadesSerializer(many=False)
    class Meta:
        model = Medicos
        fields = ["nome","crm","telefone","especialidade"]


class ConsultasSerializer(serializers.ModelSerializer):
    dia = serializers.CharField(read_only=True, source="agenda.dia")
    horario = serializers.CharField(read_only=True, source="agenda.horarios")
    medico = MedicoSerializer(source="agenda.medico", many=False)
    class Meta:
        model = Consultas
        fields = ['dia','horario','data_agendamento','medico']