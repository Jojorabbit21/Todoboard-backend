from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import HttpResponse
from .models import Board, Agenda
from .serializers import BoardSerializer, AgendaSerializer

@api_view(['GET', 'POST'])
def api_board(request):
  if request.method == 'GET':
      post = Board.objects.all()
      serialized = BoardSerializer(post, many=True)
      return Response(serialized.data)
  elif request.method == 'POST':
    serializer = BoardSerializer(data=request.data, many=True)
    if(serializer.is_valid()):
      serializer.save()
      return Response(serializer.data, status=200)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET','POST'])
def api_agenda(request):
  if request.method == 'GET':
      post = Agenda.objects.all()
      serialized = AgendaSerializer(post, many=True)
      return Response(serialized.data)
  elif request.method == 'POST':
    serializer = AgendaSerializer(data=request.data, many=True)
    if(serializer.is_valid()):
      serializer.save()
      return Response(serializer.data, status=200)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)