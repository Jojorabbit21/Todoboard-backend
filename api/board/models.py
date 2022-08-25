from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

class Board(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=50, verbose_name="Board Title")
  date_start = models.DateField(blank=False, default=timezone.now(), verbose_name="Date Start")
  date_exp = models.DateField(blank=False, default=timezone.now()+timedelta(days=7), verbose_name="Date Expiration")
  
  def __str__(self):
    return self.title
  
class Agenda(models.Model):
  parent = models.ForeignKey(Board, on_delete=models.CASCADE)
  title = models.CharField(max_length=50, verbose_name="To Do Title")
  completed = models.BooleanField(verbose_name="Completed")
  date_start = models.DateField(blank=False, default=timezone.now(), verbose_name="Date Start")
  date_exp = models.DateField(blank=False, verbose_name="Date Expiration")
  markdown = models.TextField(max_length=400, blank=True, null=True)
  
  def __str__(self):
    return self.title
  
  def is_completed(self):
    return True if self.completed == True else False
  