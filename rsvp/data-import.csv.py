# this is less a true python script, more a list of things to dump into `python manage.py shell`

import csv
import re
from rsvp import models

csvfile = open('invite-list.csv')
reader = csv.DictReader(csvfile)

for row in reader:
    row['suburb'] = re.sub(r'\s[0-9]{4}$', r'', row['suburb'])
    row['city'] = re.sub(r'\s[0-9]{4}$', r'', row['city'])
    row['invite_sent'] = True
    m = models.Invite.objects.create(**row)
    m.save()