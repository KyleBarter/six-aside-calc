from django.shortcuts import render
from django.http import HttpResponse


#! LOGIN / SIGNUP

#? login form

#? signup form


#! MAIN PAGES

#? Home
def index(request):
    return HttpResponse('Hello, world, index page')


#! Player funcs

#? Player view collection
def get_players(request):
    return HttpResponse("Hello, world! All players page")

#? Player view individual
def get_individual_player(request):
    return HttpResponse("Hello, world! Individual player page")

#? Player add
def add_player(request):
    return HttpResponse("Hello, world! Add player page")

#? Player delete

#? Player update

#? Player edit



#! Team funcs

#? Team size selector

#? Team selector