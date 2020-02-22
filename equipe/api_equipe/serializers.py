from rest_framework import serializers
from equipe.models import Especialidades, Medicos

class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidades
        fields = '__all__'

class MedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicos
        fields = '__all__'