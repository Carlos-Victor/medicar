from django.contrib import admin
from equipe.models import Agenda, Medicos, Horarios, Especialidades
# Register your models here.

class AgendaAdmin(admin.ModelAdmin):
    model = Agenda
    filter_horizontal = ('horarios',)


admin.site.register(Especialidades)
admin.site.register(Medicos)
admin.site.register(Horarios)
admin.site.register(Agenda, AgendaAdmin)