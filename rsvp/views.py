from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("This is the response form")

def respond(request, invite_id):
  return HttpResponse("This is the specfic response form for invite {0}".format(invite_id))
