from django.contrib.auth.models import User
from .models import Team, UserTeam, MyBet
from .ApiFiles import Apifoot
from django.test import TestCase


class TeamTestCase(TestCase):

    def setUp(self):
        self.team1 = Team.objects.create(
            name='One for all',
            code='tdprevfojwtdprevfojw',
            champ='Ligue 3'

        )

        self.user1 = User.objects.create(
            username= 'test_man',
            last_name= 'mister',
            first_name= 'dupont',
            email= 'dupont@gmail.com',
            password= 'test'
        )

        self.team_user = UserTeam.objects.create(id_user=self.user1,
                                                 id_team=self.team1,
                                                 points=0
                                                 )
        self.bet = MyBet.objects.create(id_user_team=self.team_user,
                                        id_match="223006",
                                        match_bet="N"
                                        )

    def test_team_code(self):
        test_team = Team.objects.get(name='One for all')
        expected_team = f'{test_team.code}'
        self.assertEqual(expected_team, 'tdprevfojwtdprevfojw')

    def test_user_team(self):

        team_user = UserTeam.objects.create(id_user=self.user1,
                                            id_team=self.team1,
                                            points=0
                                            )

        self.assertEqual(team_user.id_user, self.user1)

    def test_bet_match_id(self):
        bet = MyBet.objects.get(id=1)
        expected_team = f'{bet.id_match}'
        self.assertEqual(expected_team, '223006')


class ApiTestCase(TestCase):

    def test_fail_api(self):
        response = self.client.get('https://apiv2.apifootball.com/?action=test123&APIkey=123123')
        self.assertEqual(response.status_code, 302)

    def test_get_match_id(self):
        league = Apifoot()
        date1 = "2019-08-19"
        date2 = "2019-08-19"
        match_day = league.get_match(date1, date1)
        match = match_day[0]["match_id"]
        self.assertEqual(match, '228996')

    def test_match_finished(self):
        league = Apifoot()
        date1 = "2019-08-19"
        date2 = "2019-08-19"
        match_day = league.get_match(date1, date1)
        match = match_day[0]["match_status"]
        self.assertEqual(match, 'Finished')

    def test_get_id_list(self):
        league = Apifoot()
        date1 = "2019-08-29"
        date2 = "2019-08-31"
        list1 = ['229016', '229017', '229018', '229020', '229022', '229023', '229025', '229021']
        match_day = league.get_match(date1, date2)
        i = 0
        id_list = []
        while i < len(match_day):
            id_list.append(match_day[i]["match_id"])
            i += 1
        self.assertEqual(list1, id_list)

    def test_get_odds(self):
        league = Apifoot()
        date1 = "2019-08-21"
        date2 = "2019-08-23"
        match_odds = league.get_odds(date1, date2)
        odds_list = []
        odds2 = ['2.00', '3.30', '3.80']
        odds_list.append(match_odds[0]["odd_1"])
        odds_list.append(match_odds[0]["odd_x"])
        odds_list.append(match_odds[0]["odd_2"])
        self.assertEqual(odds_list, odds2)

