#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'ipython_log.py'})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
from django.contrib.auth.models import User, Group
user = User.objects.get(username__exact='pac_01')
user = User.objects.get(username='pac_01')
user = User.objects.get(username='pac_01')
