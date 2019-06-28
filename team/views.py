from django.shortcuts import render
from django.http import HttpResponse


def test(request):
    message = "salut tout le monde"
    return HttpResponse(message)
