from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import CreateTeamForm, JoinTeamForm
from django.shortcuts import render, redirect
from .models import Team, UserTeam
from django.contrib.auth.decorators import login_required
import random, string
from django.shortcuts import get_object_or_404


def random_string(stringLength=10):
    """
    Generate a random string of fixed length

    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


# def team_required():
#     """
#
#     A decorator which give access to the group function
#
#     """
#     pass

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


# def ranking_team(request):
#     """
#
#     Get the ranking of a group
#
#     """
#     pass
