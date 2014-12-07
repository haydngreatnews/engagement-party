from django.test import TestCase
from datetime import datetime, timedelta
import django.utils.timezone

from . import models

class ModelsTestCase(TestCase):

  def setUp(self):
    data = dict()
    data["name"] = "Libby & Haydn"
    data["informal_name"] = "Us, Stupid"
    data["street_address"] = "1/133 Dixon St"
    data["suburb"] = "Te Aro"
    data["city"] = "Wellington"
    data["postcode"] = "6011"
    data["number_invited"] = "2"
    data["invite_sent"] = True
    #data["rsvp"] = models.DateTimeField(default=None, null=True)
    #data["attending"] = models.BooleanField(default=False)
    #data["number_attending"] = models.IntegerField(default=None, null=True)
    models.Invite.objects.create(**data)

    data["name"] = "Lillie & Tom"
    data["informal_name"] = "Dem neighbour folk"
    data["street_address"] = "2/133 Dixon St"
    models.Invite.objects.create(**data)

    data["name"] = "John Pike"
    data["informal_name"] = "Pikey Pikerman"
    data["street_address"] = "150 Willis St"
    models.Invite.objects.create(**data)

  MAX_OFFSET = timedelta(seconds=10)

  def test_invites_can_rsvp(self):
    us = models.Invite.objects.get(name__exact="Libby & Haydn")
    us.process_rsvp(True, 2)
    us = models.Invite.objects.get(name__exact="Libby & Haydn")
    delta = us.rsvp - django.utils.timezone.now()
    self.assertTrue(delta < self.MAX_OFFSET)
    self.assertTrue(us.attending)
    self.assertEqual(us.number_attending, 2)

  def test_oversubscription(self):
    invite = models.Invite.objects.get(name__exact="Lillie & Tom")
    invite.process_rsvp(True, 4)
    invite = models.Invite.objects.get(name__exact="Lillie & Tom")
    delta = invite.rsvp - django.utils.timezone.now()
    self.assertTrue(delta < self.MAX_OFFSET)
    self.assertTrue(invite.attending)
    self.assertEqual(invite.number_attending, 4)
    try:
      alert = models.Alert.objects.get(invite__name="Lillie & Tom")
    except:
      self.fail()
    self.assertTrue("Lillie & Tom" in alert.reason)

  def test_not_attending(self):
    invite = models.Invite.objects.get(name__exact="John Pike")
    invite.process_rsvp(False, 4)
    invite = models.Invite.objects.get(name__exact="John Pike")
    self.assertFalse(invite.attending)
    self.assertEqual(invite.number_attending, None)
