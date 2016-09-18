from django.shortcuts import render
from django.http import JsonResponse


def index(requests):
    return render(requests, 'community/index.html')

#TODO: index.html 파일안에서 AJAX로 통신. 