from django.db import models

# Create your models here.
class Horarios(models.Model):
    horario = models.CharField("Horarios", max_length=50)

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

        def __str__(self):
            return self.horario


class Especialidades(models.Model):
    nome = models.CharField("Nome da Especialidade", max_length=50)

    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'

        def __str__(self):
            return self.nome


class Medicos(models.Model):
    nome = models.CharField("Nome do Médico", max_length=50)
    crm = models.IntegerField("Código CRM")
    email = models.EmailField("Email", max_length=254)
    telefone = models.CharField("Telefone", max_length=50)
    especialidade = models.ForeignKey("Especialidades", verbose_name=(
        "Especialidades"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'

        def __str__(self):
            return self.nome


class Agenda(models.Model):
    medico = models.ForeignKey("Medicos", verbose_name=(
        "Medico"), on_delete=models.CASCADE)
    dia = models.DateField("Dia", auto_now=False, auto_now_add=False)
    horarios = models.ManyToManyField(
        "Horarios", verbose_name=("Horarios Disponiveis"))

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'

        def __str__(self):
            return self.dia
