from django import forms
from django.utils.safestring import mark_safe
from . import models

class InviteForm(forms.ModelForm):
  choices = (
    (True, mark_safe("Yes, <span class='xwill'>I'll</span> be there like ants at a picnic!")),
    (False, mark_safe("No, sorry, the universe has conspired against <span class='xsecondp'>me</span>."))
  )
  attending = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)
  class Meta:
    model = models.Invite
    fields = ['attending', 'number_attending']

  def save(self, commit=True):
    self.instance.process_rsvp(
      self.cleaned_data['attending'],
      self.cleaned_data['number_attending']
    )
