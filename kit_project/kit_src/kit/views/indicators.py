from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from generic.sorters import SimpleSorter
from generic.views import generic
from rapidsms_xforms.models import XFormSubmission, XForm
from rapidsms_xforms.views import edit_submission,make_submission_form
from datetime import datetime
from kit.models import ApprovedSubmission

def edit_report(req, submission_id):
    submission = get_object_or_404(XFormSubmission, pk=submission_id)
    toret = edit_submission(req, submission_id)

#need to return to the view of the report not the xform view of submissions
    if type(toret) == HttpResponseRedirect:
         return redirect('/reports/%d/view/' % submission.xform.pk)
    else:
        return toret

#only allows the user to edit submissions that belong to his own group(NGO)
def view_submissions(request, xform_pk):
    xform = get_object_or_404(XForm, pk=xform_pk)
    return generic(\
        request, \
        model=XFormSubmission, \
        queryset=xform.submissions.filter(message__connection__contact__groups__in=request.user.groups.all()).order_by('-created'), \
        objects_per_page=25, \
        base_template='kit/submissions_base.html', \
        partial_row='kit/partials/reports/submission_row.html', \
        results_title='Last Reporting Period Results', \
        columns=[('Reporter', True, 'message__connection__contact__name', SimpleSorter(),), \
                 ('Location', True, 'message__connection__contact__reporting_location__name', SimpleSorter(),), \
				 ('Group', True, 'message__connection__contact__groups', SimpleSorter(),),\
                 ('Report', True, 'raw', SimpleSorter(),), \
                 ('Date', True, 'created', SimpleSorter(),), \
                 ('Approved', True, 'approved', SimpleSorter(),), \
                 ('', False, '', None,)], \
        sort_column='-created', \
    )

def toggle_approval(req, submission_id):
    submission = get_object_or_404(XFormSubmission, pk=submission_id)
    
    if(submission.approved is True):
        submission.approved = False
        appr_submission = ApprovedSubmission.objects.get(submission_id = submission)
        appr_submission.delete()
    else:
        submission.approved = True
        appr_sub = ApprovedSubmission.objects.create(submission_id = submission, time_approved= datetime.now())
        appr_sub.save()

    submission.save()
    return redirect('/reports/%d/view/' % submission.xform.pk)
