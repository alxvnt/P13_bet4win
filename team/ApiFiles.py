#! /usr/bin/env python3
# coding: utf-8

import requests


class Apifoot:

    def __init__(self):
        self.url = "https://apiv2.apifootball.com/?action="
        self.key = "70a1b277077102cde419bf66e69fe71f62b476110606efb3e62666c8ec0b3dab"
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

    def get_odds(self, date1, date2):
        action = "get_odds&from="
        response = requests.get(self.url + action + date1 + "&to=" + date2 +
                                "&APIkey=" + self.key)
        resp_json = response.json()
        try:
            return resp_json
        except IndexError:
            return "1"


def main():
    gmap = Apifoot()
    date1 = "2019-07-29"
    date2 = "2019-08-02"
    standing = gmap.get_odds(date1, date2)
    i=0

    print(standing[i]["odd_1"])
    print(standing[i]["odd_x"])
    print(standing[i]["odd_2"])
    #    print(country[i]["match_hometeam_name"] + " vs " + country[i]["match_awayteam_name"])
    #    i+=1

#main()


week_dict = {
"1" : ["2019-07-22"],
"2" : ["2019-07-29"],
"3" : ["2019-08-05"],
"4" : ["2019-08-12"],
"5" : ["2019-08-19"],
"6" : ["2019-08-26"],
"7" : ["2019-09-02"],
"8" : ["2019-09-09"],
"9" : ["2019-09-16"],
"10" : ["2019-09-23"],
"11" : ["2019-09-30"],
"12" : ["2019-10-14"],
"13" : ["2019-10-21"],
"14" : ["2019-10-28"],
"15" : ["2019-11-04"],
"16" : ["2019-11-18"],
"17" : ["2019-11-25"],
"18" : ["2019-12-02"],
"19" : ["2019-12-09"],
"20" : ["2020-12-16"],
"21" : ["2020-01-06"],
"22" : ["2020-01-20"],
"23" : ["2020-01-27"],
"24" : ["2020-02-03"],
"25" : ["2020-02-10"],
"26" : ["2020-02-17"],
"27" : ["2020-02-24"],
"28" : ["2020-03-02"],
"29" : ["2020-03-09"],
"30" : ["2020-03-16"],
"31" : ["2020-03-30"],
"32" : ["2020-04-06"],
"33" : ["2020-04-13"],
"34" : ["2020-04-20"],
"35" : ["2020-04-27"],
"36" : ["2020-05-04"],
"37" : ["2020-05-11"]

}
