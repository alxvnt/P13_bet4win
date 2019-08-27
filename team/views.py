from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import CreateTeamForm, JoinTeamForm, DayChampForm
from django.shortcuts import render, redirect
from .models import Team, UserTeam, MyBet
from django.contrib.auth.decorators import login_required
import random
import string
import datetime
from datetime import date, datetime, timedelta
from .ApiFiles import Apifoot


def random_string(stringLength=10):
    """
    Generate a random string of fixed length

    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def team_required(fonct):
    """

    A decorator which give access to the group function

    """
    def error_fonction(*param):
        # request = param[0]
        print(param)
        # current_user = request.user
        # current_team = UserTeam.objects.filter(id_user=current_user, id_team=param[1])
        # if current_team:
        #     return fonct
        # else:
        #     return team_error

    return error_fonction()


@login_required
def new_team(request):
    """

     Create a new team
    """
    if request.method == 'POST':
        form = CreateTeamForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            champ = form.cleaned_data['champ']
            code = random_string(20)
            creator = request.user
            team = Team.objects.create(name=name,
                                       code=code,
                                       champ=champ
                                       )
            team_user = UserTeam.objects.create(id_user=creator,
                                                id_team=team,
                                                points=0
                                                )
            return redirect('/connexion')

    else:
        form = CreateTeamForm()

    return render(request, 'team/new_group.html', locals())


@login_required
def my_groups(request):
    """
    Get all the groups of a user

    """
    current_user = request.user
    user_list = UserTeam.objects.filter(id_user=current_user)
    team_list = []

    for i in user_list:
        team = Team.objects.get(name=i.id_team)
        team_list.append(team)
    return render(request, 'users/my_groups.html', locals())


@login_required
def join_group(request):
    """
    Join a group with the key team
     
    """
    error = 0
    if request.method == 'POST':
        form = JoinTeamForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data['teamKey']
            team = Team.objects.filter(code=key)
            current_user = request.user
            if team:
                test_team = UserTeam.objects.filter(id_user=current_user,
                                                    id_team=team[0]
                                                    )
                if not test_team:
                    create_team = UserTeam.objects.create(id_user=current_user,
                                                          id_team=team[0],
                                                          points=0
                                                         )
                else:
                    error = 2
            else:
                error = 3
                form = JoinTeamForm()
    else:
        form = JoinTeamForm()
    return render(request, 'team/join_group.html', locals())


def leave_team(request):
    """

    Delete the access to a team for the current user

    """
    if request.method == 'POST':

        current_user = request.user
        team_name = request.POST.get('delete_team')
        team_to_leave = Team.objects.get(name=team_name)
        UserTeam.objects.get(id_user=current_user, id_team=team_to_leave).delete()
        return redirect('/mes-groupes')

    return render(request, 'users/my_groups.html', locals())


def ranking_team(request, team_name):
    """

    Get the ranking of a group

    """
    current_user = request.user
    active_team = 1
    select_team = Team.objects.filter(name=team_name)
    if not select_team:
        return render(request, 'team/team_error.html', locals())
    current_team = UserTeam.objects.filter(id_team=select_team[0], id_user=current_user)
    if not current_team:
        return render(request, 'team/team_error.html', locals())

    team_member = UserTeam.objects.filter(id_team=select_team[0])

    return render(request, 'team/team_ranking.html', locals())


def team_error(request):

    return render(request, 'team/team_error.html', locals())


@login_required
def champ(request, team_name):
    current_user = request.user
    active_team = 1
    select_team = Team.objects.filter(name=team_name)
    if not select_team:
        return render(request, 'team/team_error.html', locals())
    current_team = UserTeam.objects.filter(id_team=select_team[0], id_user=current_user)
    if not current_team:
        return render(request, 'team/team_error.html', locals())

    league = Apifoot()
    standing = league.get_champ_info()
    i = 0
    league_dict = {}
    while i < 20:
        league_dict[standing[i]["team_name"]] = [standing[i]["overall_league_PTS"], standing[i]["overall_league_W"],
                                                 standing[i]["overall_league_D"], standing[i]["overall_league_L"],
                                                 standing[i]["overall_league_position"]]

        i += 1
    return render(request, 'team/championship.html', locals())


@login_required
def day_match(request, team_name):
    current_user = request.user
    active_team = 1
    select_team = Team.objects.filter(name=team_name)
    if not select_team:
        return render(request, 'team/team_error.html', locals())
    current_team = UserTeam.objects.filter(id_team=select_team[0], id_user=current_user)
    if not current_team:
        return render(request, 'team/team_error.html', locals())

    if request.method == 'POST':
        form = DayChampForm(request.POST)
        if form.is_valid():
            form_date = form.cleaned_data['date']

            day = datetime.strptime(form_date, '%Y-%m-%d')
            league = Apifoot()
            x = timedelta(days=7)
            week = day + x
            match_day = league.get_match(str(day), str(week))

            i = 0
            league_dict = {}
            while i < 9:
                league_dict[i] = [match_day[i]["match_date"], match_day[i]["match_time"], match_day[i]["match_hometeam_name"],
                                  match_day[i]["match_hometeam_score"], match_day[i]["match_awayteam_score"],
                                  match_day[i]["match_awayteam_name"]]
                i += 1

    else:
        form = DayChampForm()
        league = Apifoot()
        today = date.today()

        x = timedelta(days=7)
        week = today + x
        match_day = league.get_match(str(today), str(week))
        i = 0
        league_dict = {}
        while i < 9:
            league_dict[i] = [match_day[i]["match_date"], match_day[i]["match_time"],
                              match_day[i]["match_hometeam_name"],
                              match_day[i]["match_hometeam_score"], match_day[i]["match_awayteam_score"],
                              match_day[i]["match_awayteam_name"]]
            i += 1
    return render(request, 'team/match_of_the_day.html', locals())


def match_to_bet(request, team_name):
    current_user = request.user
    active_team = 1
    select_team = Team.objects.filter(name=team_name)
    if not select_team:
        return render(request, 'team/team_error.html', locals())
    current_team = UserTeam.objects.filter(id_team=select_team[0], id_user=current_user)
    if not current_team:
        return render(request, 'team/team_error.html', locals())

    league = Apifoot()
    #today = date.today()
    today = "2019-08-21"
    week = "2019-08-23"
    x = timedelta(days=3)
    #week = today + x
    # get 2 json which contains odds list and match details
    match_day = league.get_match(str(today), str(week))
    match_odds = league.get_odds(str(today), str(week))
    i = 0

    # ajouter la partie de récupération des odds
    # if match_day[0]:
    #     league_dict = {}
    #     while i < len(match_day):
    #         league_dict[i] = [match_day[i]["match_id"], match_day[i]["match_date"], match_day[i]["match_hometeam_name"],
    #                           match_day[i]["match_awayteam_name"]]
    #
    #         i += 1

    # Get a list of the id from the match
    if match_day[0]:
        league_dict = {}
        id_list = []
        while i < len(match_day):
            id_list.append(match_day[i]["match_id"])
            i += 1
        dic_odds = {}
        # initalize counter to browse id_list
        z = 0
        for x in id_list:
            y = 0
            while y < len(match_odds):
                if match_odds[y]["match_id"] == x:
                    dic_odds[id_list[z]] = [match_odds[y]["odd_1"], match_odds[y]["odd_x"], match_odds[y]["odd_2"]]
                    y = len(match_odds)
                y += 1
            z += 1
        league_dict = {}
        f = 0
        while f < len(match_day):
            league_dict[f] = [match_day[f]["match_date"], match_day[f]["match_hometeam_name"],
                              match_day[f]["match_awayteam_name"],
                              dic_odds[match_day[f]["match_id"]][0],
                              dic_odds[match_day[f]["match_id"]][1],
                              dic_odds[match_day[f]["match_id"]][2],
                              match_day[f]["match_id"]
                              ]
            f += 1
    return render(request, 'team/match_to_bet.html', locals())


def my_bet(request, team_name, id_match, prono):

    current_user = request.user
    team = Team.objects.get(name=team_name)
    user_info = UserTeam.objects.get(id_user=current_user, id_team=team)

    bet = MyBet.objects.filter(id_user_team=user_info, id_match=id_match)
    if bet:
        error = 1
    else:
        new_bet = MyBet(id_user_team=user_info, id_match=id_match, match_bet=prono)
        new_bet.save()
        error = 0
    return render(request, 'team/bet_validate.html', locals())