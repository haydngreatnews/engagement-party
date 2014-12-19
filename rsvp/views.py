from django.shortcuts import render,  render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView


import json

from . import models
from . import forms

def index(request):
  context = RequestContext(request)
  rendered = render_to_response('search.html', context)
  return rendered

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
      'invite_id': invite.id,
      'slug': invite.slug,
    }
    resultset.append(result)

  return HttpResponse(json.dumps(resultset))

def thanks(request):
  context = RequestContext(request)
  rendered = render_to_response('thanks.html', context)
  return rendered

class InviteReturnView(UpdateView):
  template_name = 'rsvp_form.html'
  model = models.Invite
  form_class = forms.InviteForm

  def get_success_url(self):
    return reverse('thanks')
