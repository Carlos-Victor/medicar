from rest_framework import serializers
from consulta.models import Consultas
from equipe.models import Medicos, Agenda
from rest_framework.serializers import ModelSerializer, SlugRelatedField, StringRelatedField, HyperlinkedIdentityField, ValidationError
from expander import ExpanderSerializerMixin





# agenda = StringRelatedField(
#     slug_field='dia',
#     read_only=True,
#     queryset=Agenda.objects.all()
# )


class MedicoSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Medicos
        fields = '__all__'


class ConsultasSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    dia = serializers.CharField(read_only=True, source="agenda.dia")
    horario = serializers.CharField(read_only=True, source="agenda.horarios")
    # agenda = SlugRelatedField(
    #     slug_field='dia',
    #     queryset=Agenda.objects.all()
    # )
    class Meta:
        model = Consultas
        fields = ['paciente', 'dia','horario','data_agendamento']
        expandable_fields = {
            'medico': MedicoSerializer
        } 
        # fields = '__all__'