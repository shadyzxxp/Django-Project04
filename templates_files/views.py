import re
import requests
from datetime import datetime

from django.shortcuts import render

from templates_files.models import *
from templates_files.api import ApiHeadHunter



def home_page(request):
    return render(request, 'HomePage.html',
                  { 'context': MainPage.objects.all()})


def demand_page(request):
    return render(request, 'Demend.html', { 'context': Demand.objects.all()})


def geography_page(request):
    return render(request, 'Geography.html',
                  { 'context': Geography.objects.all()})


def skills_page(request):
    return render(request, 'Skills.html', { 'context': Skills.objects.all()})


def last_vacancy_page(request):
    hh = ApiHeadHunter('php-разработчик')
    vacs = hh.get_data_vacancies('2024-01-15', 10)

    context = {'vacs': vacs}

    return render(request, 'LastVacancy.html', context)
