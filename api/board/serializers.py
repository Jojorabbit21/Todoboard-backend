from rest_framework import serializers
from .models import Board, Agenda

class AgendaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Agenda
    fields = ('id', 'parent', 'title', 'completed', 'date_start', 'date_exp', 'markdown')
    
class BoardSerializer(serializers.ModelSerializer):
  agendas = AgendaSerializer(many=True, read_only=True)
  class Meta:
    model = Board
    fields = ('id', 'title', 'date_start', 'date_exp', 'agendas')
    