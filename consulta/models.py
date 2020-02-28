from django.db import models
from django.contrib.auth.models import User
from equipe.models import Medicos, Agenda
from django.contrib.auth import get_user_model


# Create your models here.


class Consultas(models.Model):
    paciente = models.ForeignKey(get_user_model(), verbose_name=("Paciente"), on_delete=models.CASCADE)
    agenda = models.ForeignKey("equipe.Agenda", verbose_name=("dia"), on_delete=models.CASCADE)
    horario = models.CharField("Horário", max_length=6)
    data_agendamento = models.DateTimeField("Data do Agendamento", auto_now=True)