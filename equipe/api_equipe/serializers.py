from rest_framework import serializers
from equipe.models import Especialidades, Medicos, Agenda


class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidades
        fields = '__all__'


class MedicosSerializer(serializers.ModelSerializer):
    especialidade = EspecialidadesSerializer(many=False)

    class Meta:
        model = Medicos
        fields = ["nome", "crm", "telefone", "especialidade"]


class AgendaSerializer(serializers.ModelSerializer):
    horarios = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='horario'
    )
    medico = MedicosSerializer(many=False)

    class Meta:
        model = Agenda
        fields = ["id", "medico", "dia", "horarios"]
