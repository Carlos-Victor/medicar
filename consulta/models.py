from django.db import models
from django.contrib.auth.models import User
from equipe.models import Medico, Agenda
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from datetime import datetime
from rest_framework import serializers


# Create your models here.


class Consulta(models.Model):
    paciente = models.ForeignKey(get_user_model(), verbose_name=("Paciente"), on_delete=models.CASCADE)
    agenda = models.ForeignKey("equipe.Agenda", verbose_name=("dia"), on_delete=models.CASCADE)
    horario = models.CharField("Horário", max_length=6)
    data_agendamento = models.DateTimeField("Data do Agendamento", auto_now=True)

    def __str__(self):
        return f'{self.paciente}, Médico:{self.agenda.medico}, Dia: {self.agenda.dia}, horario: {self.horario}, data do agendamento:{self.data_agendamento} '

    def clean(self):
        if Agenda.objects.filter(medico=self.agenda.medico, horarios__horario=self.horario).exists() == False:
            raise serializers.ValidationError({"detail":"Este horário não existe na agenda do médico"})

        elif self.horario < f'{datetime.today().hour}:{datetime.today().minute}':
            raise serializers.ValidationError('Não foi possivel Marcar uma consulta, horário é menor que a hora atual')

        elif Consulta.objects.filter(agenda__dia=self.agenda.dia, horario=self.horario, paciente=self.paciente).exists():
            raise serializers.ValidationError({"detail":"Paciente já possui uma consulta marcada para esse mesmo dia e horário"})

        elif Consulta.objects.filter(agenda__dia=self.agenda.dia, horario=self.horario).exists():
            raise serializers.ValidationError({"detail":"Já possui uma consulta marcada para um paciente no mesmo dia e horário"})