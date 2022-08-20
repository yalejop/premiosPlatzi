from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Estás en la página principal de Premios Platzi App')

def detail(request, question_id):
    return HttpResponse(f'Estas viendo la pregunta número {question_id}')

def result(request, question_id):
    return HttpResponse(f'Estas viendo los resultados de la pregunta número {question_id}')

def vote(request, question_id):
    return HttpResponse(f'Estas votando a la pregunta número {question_id}')