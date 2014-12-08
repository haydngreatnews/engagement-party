from django.shortcuts import render
from django.http import HttpResponse

import json

def index(request):
  return HttpResponse("This is the response form")

def respond(request, invite_id):
  return HttpResponse("This is the specfic response form for invite {0}".format(invite_id))

def search(request):
  qry = request.GET.get('q', '')
  resultset = []
  result = dict()
  result["match"] = "name"
  result["name"] = "Errol & Rosie"
  result["informal"] = "Mum & Dad"
  result["invite_id"] = 8
  result["search_string"] = qry
  resultset.append(result)
  resultset.append(result)

  return HttpResponse(json.dumps(resultset))
