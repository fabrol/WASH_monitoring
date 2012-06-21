from django.db import models
from rapidsms.models import ContactBase
class ExtendedContact(models.Model):

	reporting_location = models.ForeignKey('locations.Location', blank=True, null=True)
    def total_submissions(self):
        from rapidsms_xforms.models import XFormSubmission
        return XFormSubmission.objects.filter(connection__in=self.connection_set.all(), has_errors=False).count()

    class Meta:
        abstract = True
