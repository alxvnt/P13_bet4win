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
from django.test import TestCase
from django.contrib.auth import authenticate
from django.urls import reverse


class GroupTestCase(TestCase):

    def setUp(self):
        self.new_user = User.objects.create(email="nouveau@test.com", password="new_password")
        self.logging = authenticate(email="nouveau@test.com", password="new_password")

    def test_my_group(self):
        login = self
        response = self.client.get(reverse('my_groups'))
        self.assertEqual(response.status_code, 200)


class ApiTestCase(TestCase):

    def test_fail_api(self):
        response = self.client.get('https://apiv2.apifootball.com/?action=test123&APIkey=123123')
        self.assertEqual(response.status_code, 404)


class BetTestCase(TestCase):
    pass
