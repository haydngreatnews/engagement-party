from django.db import models
from datetime import datetime
import django.utils.timezone

class Invite(models.Model):
  name = models.CharField(max_length=255)
  informal_name = models.CharField(max_length=255)
  street_address = models.CharField(max_length=255)
  suburb = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  postcode = models.CharField(max_length=255)
  number_invited = models.IntegerField(default=1)
  invite_sent = models.BooleanField(default=False)
  rsvp = models.DateTimeField(default=None, null=True, blank=True)
  attending = models.BooleanField(default=False, blank=True)
  number_attending = models.IntegerField(default=None, null=True, blank=True)

  def process_rsvp(self, attending, number_attending):
    self.attending = attending
    self.rsvp = django.utils.timezone.now()
    if attending:
      self.number_attending = number_attending
      if number_attending > self.number_invited:
        reason = "The invited group {0} has stated that {1} people will be attending, rather than the expected {2}".format(
          self.name, number_attending, self.number_invited)
        Alert.objects.create(reason=reason, invite=self)
    self.save()
    return;

class Alert(models.Model):
  reason = models.TextField()
  invite = models.ForeignKey('Invite')
  timestamp = models.DateTimeField(auto_now_add=True)
