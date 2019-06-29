from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import CreateTeamForm
from django.shortcuts import render, redirect
from .models import Team, UserTeam
from django.contrib.auth.decorators import login_required
import random, string


def test(request):
    message = "salut tout le monde"
    return HttpResponse(message)


def random_string(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


@login_required
def new_team(request):
    if request.method == 'POST':
        form = CreateTeamForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            champ = form.cleaned_data['champ']
            code = random_string(20)
            creator = request.user
            team = Team.objects.create(name=name,
                                       code=code,
                                       champ=champ,
                                       creator=creator
                                       )
            team_user = UserTeam.objects.create(id_user=creator,
                                                id_team=team,
                                                points=0
                                                )
            return redirect('/connexion')

    else:
        form = CreateTeamForm()

    return render(request, 'team/new_group.html', locals())
