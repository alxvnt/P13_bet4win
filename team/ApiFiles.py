#! /usr/bin/env python3
# coding: utf-8

import requests


class Apifoot:

    def __init__(self):
        self.url = "https://apiv2.apifootball.com/?action="
        self.key = "b4c5e97527e702485d19bafdd799a24b57b79e2bdc68f0dd36c52012016e8cde"
        self.id_league = "177"

    # return the lat and the lng of the attribute question
    def get_all_country(self):
        action = "get_countries"
        response = requests.get(self.url + action + "&APIkey=" + self.key)
        resp_json = response.json()
        try:
            return resp_json[1]["country_id"]
        except IndexError:
            return "1"

    def get_match(self, date1, date2):
        action = "get_events&from="
        response = requests.get(self.url + action + date1 + "&to=" + date2 +
                                "&league_id=" + self.id_league + "&APIkey=" + self.key)
        resp_json = response.json()
        try:
            return resp_json
        except IndexError:
            return "1"

    def get_champ_info(self):
        action = "get_standings"
        response = requests.get(self.url + action +
                                "&league_id=" + self.id_league + "&APIkey=" + self.key)
        resp_json = response.json()
        try:
            return resp_json
        except IndexError:
            return "1"

    def get_team_result(self):
        pass


def main():
    gmap = Apifoot()
    date1 = "2019-08-19"
    date2 = "2019-08-26"
    #country = gmap.get_match(date1, date2)
    standing = gmap.get_champ_info()
    i=0
    while i < 20:
        print(standing[i]["team_name"] + " point : " + standing[i]["overall_league_PTS"])
        i+=1
    #    print(country[i]["match_hometeam_name"] + " vs " + country[i]["match_awayteam_name"])
    #    i+=1

main()

####################
# Récupérer matchs de la semaine + les odds
# Récupérer matchs du mois dernier
#
###################