from django.db import models
from django.contrib.auth.models import User
from equipe.models import Medicos, Agenda
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from datetime import date
from datetime import datetime
from rest_framework import serializers


# Create your models here.


class Consultas(models.Model):
    paciente = models.ForeignKey(get_user_model(), verbose_name=("Paciente"), on_delete=models.CASCADE)
    agenda = models.ForeignKey("equipe.Agenda", verbose_name=("dia"), on_delete=models.CASCADE)
    horario = models.CharField("Horário", max_length=6)
    data_agendamento = models.DateTimeField("Data do Agendamento", auto_now=True)

    def clean(self):
        if Agenda.objects.filter(medico=self.agenda.medico, horarios__horario=self.horario).exists() == False:
            raise serializers.ValidationError({"detail":"Este horário não existe na agenda do médico"})
        elif Consultas.objects.filter(agenda__dia=self.agenda.dia, horario=self.horario, paciente=self.paciente).exists():
            raise serializers.ValidationError({"detail":"Paciente já possui uma consulta marcada para esse mesmo dia e horário"})
        elif Consultas.objects.filter(agenda__dia=self.agenda.dia, horario=self.horario).exists():
            raise serializers.ValidationError({"detail":"Já possui uma consulta marcada para um paciente no mesmo dia e horário"})





        # raise Exception(self.agenda.medico)

    
    # def save(self):
    #     pass