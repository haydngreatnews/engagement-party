from django.contrib import admin

from . import models

class InviteAdmin(admin.ModelAdmin):
  exclude = ('rsvp', 'attending', 'number_attending')
  list_display = ('name','informal_name', 'rsvp', 'number_attending')
  #list_filter = ('
  search_fields = ['name', 'informal_name']
  readonly_fields = ('rsvp', 'attending', 'number_attending')

class AlertAdmin(admin.ModelAdmin):
  list_display = ('timestamp', 'reason', 'invitee')

  def invitee(self, obj):
    return obj.invite.informal_name

admin.site.register(models.Invite, InviteAdmin)
admin.site.register(models.Alert, AlertAdmin)
