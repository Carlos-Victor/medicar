from django.contrib import admin
from equipe.models import Agenda, Medico, Horario, Especialidade
# Register your models here.

class AgendaAdmin(admin.ModelAdmin):
    model = Agenda
    filter_horizontal = ('horarios',)


admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Horario)
admin.site.register(Agenda, AgendaAdmin)