from django.shortcuts import get_object_or_404
from django.utils.datastructures import SortedDict
from kit.excel.export.util import get_district
from rapidsms_xforms.models import XForm, XFormSubmission
from uganda_common.utils import ExcelResponse
from django.http import HttpResponse

def export_submissions(request, xform_pk):
    if not request.user.is_staff:
       res = HttpResponse("Unauthorized")
       res.status_code = 401
       return res
    export_data_list = []
    xform = get_object_or_404(XForm, pk=xform_pk)
    for r in XFormSubmission.objects.exclude(connection=None).filter(xform=xform):
        export_data = SortedDict()
        export_data['report_id'] = r.pk
        export_data['report'] = r.xform.name
        export_data['date'] = str(r.created)
        if r.connection.contact:
            export_data['reporter'] = r.connection.contact.name    
            export_data['reporter_id'] = r.connection.contact.pk 
            for group in r.connection.contact.groups.all():
			    export_data['NGO'] = group.name
            export_data['location'] = r.connection.contact.reporting_location.name 
            export_data['location_id'] = r.connection.contact.reporting_location.pk
        else :
            export_data['reporter'] = 'None'
            export_data['reporter_id'] = 'None'
            export_data['NGO'] = 'None'
            export_data['location'] = 'None'
            export_data['location_id'] = 'None'
        
        export_data['phone'] = r.connection.identity
        export_data['valid'] = (r.has_errors and "No") or "Yes"
        export_data['Approved'] = r.approved
        for f in xform.fields.order_by('order'):
            export_data["%s:%s" % (f.command, f.description)] = getattr(r.eav, f.slug) or 'None'

        export_data_list.append(export_data)

    return ExcelResponse(export_data_list)


def export_responses(request, poll_pk):
    pass
