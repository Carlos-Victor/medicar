from rest_framework import serializers
from equipe.models import Especialidade, Medico, Agenda


class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = '__all__'


class MedicoSerializer(serializers.ModelSerializer):
    especialidade = EspecialidadeSerializer(many=False)

    class Meta:
        model = Medico
        fields = ["nome", "crm", "telefone", "especialidade"]


class AgendaSerializer(serializers.ModelSerializer):
    horarios = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='horario'
    )
    medico = MedicoSerializer(many=False)

    class Meta:
        model = Agenda
        fields = ["id", "medico", "dia", "horarios"]
