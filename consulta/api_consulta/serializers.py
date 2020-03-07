from rest_framework import serializers
from equipe.api_equipe.serializers import MedicosSerializer
from consulta.models import Consultas

class ConsultasSerializer(serializers.ModelSerializer):
    dia = serializers.CharField(read_only=False, source="agenda.dia")
    medico = MedicosSerializer(source="agenda.medico", many=False, read_only=False)

    class Meta:
        # def validacao_dia(value):
        #     raise Exception(dict(value))
        model = Consultas
        fields = ['id','dia','horario','data_agendamento','medico']