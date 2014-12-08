from django.shortcuts import render
from django.http import HttpResponse

import json

def index(request):
  return HttpResponse("This is the response form")

def respond(request, invite_id):
  return HttpResponse("This is the specfic response form for invite {0}".format(invite_id))

def search(request, query):

  return HttpResponse("""[{
    "match": "name",
    "name": "Errol & Rosie",
    "informal" : "Mum & Dad",
    "invite_id" : 8
    }]""")
