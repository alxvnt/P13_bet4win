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
        print(id)
        list = MyBet.objects.filter(id_match=id, bet_validate=False)

        y = 0
        # on récupère dans match result l'id du match
        res = None
        #print(match_result)
        while y < len(match_result):
            #print(match_result[y]["match_id"])
            if match_result[y]["match_id"] == str(id):
                res = match_result[y]
                print(match_result[y])
                break;

            else:
                y += 1
        z = 0
        while z < len(odds):
            if match_result[z]["match_id"] == str(id):
                odds_data = odds[z]
                print(odds_data[z])
                break;

            else:
                z += 1
        print("test")
        if res["match_hometeam_score"] > res["match_awayteam_score"]:
            bet.result = 1
            bet.save()
        elif res["match_hometeam_score"] < res["match_awayteam_score"]:
            bet.result = 2
            bet.save()
        else:
            bet.result = "N"
            bet.save()

        if bet.result == bet.match_bet:

        # on récupère l'id dans match odds et la cote correspondante
        # on récupère le user team et on augemente ses points de cote *100
            if bet.result == "1":
                point = float(odds_data["odd_1"]) * 100
            elif bet.result == "2":
                point = float(odds_data["odd_2"]) * 100
            else:
                point = float(odds_data["odd_x"]) * 100

            id_user_team = bet.id_user_team
            usr_point = UserTeam.objects.get(id=id_user_team)
            usr_point.points += point
            usr_point.save()

        bet.bet_validate = True
        bet.save()

    def handle(self, *args, **options):
        league = Apifoot()
        today = date.today()
        x = timedelta(days=1)
        day = today - x
        waiting_bet = MyBet.objects.filter(bet_validate=False)
        match_result = league.get_match(str(day), str(today))
        match_odds = league.get_odds(str(day), str(today))
        if match_result and waiting_bet:
            for c in waiting_bet:
                self.bet_actualize(match_result, c, match_odds)
