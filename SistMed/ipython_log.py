#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'ipython_log.py'})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
 from django.contrib.auth.models import Group as DjangoGroup 
        gUsers = DjangoGroup(name='Users') 
        gUsers.save() 
        gGroupAdmins = DjangoGroup(name='GroupAdmins') 
        gGroupAdmins.save() 
        # Set users 
        zen = User.objects.create_user('zen', 'zen@emailaddress', 
'pwd123') 
        zen.groups = [gUsers] 
from django.contrib.auth.models import Group
g = Group.objects.get(name='Pacientes')
g
