from django.shortcuts import render,  render_to_response
from django.http import HttpResponse
from django.template import RequestContext

import json

from . import models

def index(request):
  context = RequestContext(request)
  rendered = render_to_response('search.html', context)
  return rendered

def respond(request, invite_id):
  return HttpResponse("This is the specfic response form for invite {0}".format(invite_id))

def search(request):
  qry = request.GET.get('q', '')

  resultset = []
  search_results = models.Invite.search(qry)
  if len(qry) < 2 or len(search_results) == 0:
    return HttpResponse('[]')
  for invite in search_results:
    result = {
      'name': invite.name,
      'informal': invite.informal_name,
      'invite_id' : invite.id
    }
    resultset.append(result)

  return HttpResponse(json.dumps(resultset))
