from django.contrib import admin

from .models import Board, Agenda

class AgendaInline(admin.StackedInline):
  model = Agenda
  extra = 1

class BoardAdmin(admin.ModelAdmin):
  inlines = [AgendaInline, ]
  list_display = ('title', 'date_start', 'date_exp')

admin.site.register(Board, BoardAdmin)