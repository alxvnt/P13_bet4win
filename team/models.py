from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=20, unique=True)
    champ = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class UserTeam(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user in this group')
    id_team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='a group of the user')
    points = models.DecimalField(max_digits=5, decimal_places=2)


class MyBet(models.Model):
    id_user_team = models.ForeignKey(UserTeam, on_delete=models.CASCADE, verbose_name='id of the user and his group')
    id_match = models.CharField(max_length=10, unique=True)
    match_bet = models.CharField(max_length=1)
    result = models.CharField(max_length=1, null=True)
    bet_validate = models.BooleanField(default=False)
