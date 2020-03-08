from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.
class Horario(models.Model):
    horario = models.CharField("Horarios", max_length=6)
    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self):
        return self.horario


class Especialidade(models.Model):
    nome = models.CharField("Nome da Especialidade", max_length=50)

    def clean(self):
        if Especialidade.objects.filter(nome=self.nome).exists():
            raise ValidationError('Essa Especilidade já existe')

    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return self.nome


class Medico(models.Model):
    nome = models.CharField("Nome do Médico", max_length=50)
    crm = models.IntegerField("Código CRM")
    email = models.EmailField("Email", max_length=50, null=True, blank=True)
    telefone = models.CharField("Telefone", max_length=50, null=True, blank=True)
    especialidade = models.ForeignKey("Especialidade", verbose_name=(
        "Especialidades"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'

    def __str__(self):
        return self.nome


class Agenda(models.Model):
    medico = models.ForeignKey("Medico", verbose_name=(
        "Medico"), on_delete=models.CASCADE)
    dia = models.DateField("Dia", auto_now=False, auto_now_add=False)
    horarios = models.ManyToManyField(
        "Horario", verbose_name=("Horarios Disponiveis"))
    
    def clean(self):
        if self.dia < date.today():
            raise ValidationError('Não foi possivel criar uma agenda, data inferior que o dia de hoje')
    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'

    def __str__(self):
        return f'{self.dia}, Médico: {self.medico}'
