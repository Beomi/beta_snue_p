from django.shortcuts import render
from django.http import JsonResponse


def index(requests):
    return render(requests, '')