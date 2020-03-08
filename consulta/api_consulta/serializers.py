from rest_framework import serializers
from equipe.api_equipe.serializers import MedicoSerializer
from consulta.models import Consulta

class ConsultaSerializer(serializers.ModelSerializer):
    dia = serializers.CharField(read_only=False, source="agenda.dia")
    medico = MedicoSerializer(source="agenda.medico", many=False, read_only=False)

    class Meta:
        model = Consulta
        fields = ['id','dia','horario','data_agendamento','medico']