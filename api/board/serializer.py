from rest_framework import serializers
from .models import Board, Agenda

class BoardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Board
    fields = ['id', 'title', 'date_start', 'date_exp']