from ...models import MyBet, Team, UserTeam
import requests
import django
from ...ApiFiles import *
from django.core.management.base import BaseCommand, CommandError
from datetime import date, datetime, timedelta


class Command(BaseCommand):
    help = "actualize and add the points to the player"

    def bet_actualize(self, match_result, bet, odds):
        # on récupère l'id de l'objet bet
        id = bet.id_match
        # on récupère dans match result l'id du match
        i = 0
        #while i < len(match_result):
        match = match_result[]
        # si le score hometeam > awayteam
        # bet.result = 1
        # si le score hometeam < awaayteam
        # bet.result = 2
        # else
        # bet result = N
        # if bet.result = bet.match_bet
        # on récupère l'id dans match odds et la cote correspondante
        # on récupère le user team et on augemente ses points de cote *100
        # on passe la valeur True à bet validate

    def handle(self, *args, **options):
        league = Apifoot()
        today = date.today()
        x = timedelta(days=1)
        day = today - x
        waiting_bet = MyBet.objects.filter(bet_validate=False)
        match_result = league.get_match(day, day)
        match_odds = league.get_odds(day, day)
        if match_result and waiting_bet:
            for c in waiting_bet:
                self.bet_actualize(match_result, c, match_odds)