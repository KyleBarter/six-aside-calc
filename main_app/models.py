from django.db import models

# Create your models here.
class Teams(models.Model):
    team1_name = models.CharField(max_length=200)
    team2_name = models.CharField(max_length=200)
    team_size = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Player(models.Model):
    name = models.CharField(max_length=200)
    overall = models.IntegerField(default=0)
    shooting = models.IntegerField(default=0)
    defence = models.IntegerField(default=0)
    passing = models.IntegerField(default=0)
    dribbling = models.IntegerField(default=0)
    fitness = models.IntegerField(default=0)
    team = models.ForeignKey(Teams, on_delete=models.DO_NOTHING, null=True)