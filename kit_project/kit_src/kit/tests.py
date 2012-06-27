from django.conf import settings
from django.test import TestCase
from rapidsms.models import Connection, Backend, Contact
from rapidsms.contrib.locations.models import Location, LocationType
from rapidsms_xforms.models import *
from rapidsms.messages.incoming import IncomingMessage, OutgoingMessage
from rapidsms_httprouter.models import Message


class ModelTest(TestCase):
    def setup(self):
        """
        The setup method mimics the actual setup of the server. This should give you a basic environment in which
        you run tests that are almost the same as your production environment.

        For tests in the other rapidsms super repos, they usually tend to be pretty stable. For example, you don't need
        to test rapidsms-xforms unless you feel it is broken.
        """
        if 'django.contrib.sites' in settings.INSTALLED_APPS:
            site_id = getattr(settings, 'SITE_ID', 5)
            Site.objects.get_or_create(pk=site_id, defaults={'domain':'rapidsmsmada.org'})
            fixtures['initial_data.json']

        User.objects.get_or_create(username = 'admin')
        self.backend = Backend.objects.create(name = 'test')
        self.connection = Connection.objects.create(identity='12345', backend=self.backend)
        country = LocationType.objects.create(name = 'country', slug = 'country')
        region = LocationType.objects.create(name = 'region', slug = 'region')
        district = LocationType.objects.create(name = 'district', slug = 'district')
        commune = LocationType.objects.create(name = 'commune', slug = 'commune')
        fokontany = LocationType.objects.create(name = 'fokontany', slug = 'fokontany')
        # it appears that the village data will be quite a focus given the extent of the pilot program and phase
        village = LocationType.objects.create(name = 'village', slug='village')

#### add more methods; look at example code in other projects.