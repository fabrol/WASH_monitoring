from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from generic.views import generic, generic_row
from generic.sorters import SimpleSorter
from kit.excel.upload.views import bulk_upload
from contact.forms import AssignGroupForm, MassTextForm
from contact.urls import urlpatterns as contact_urls
from kit.views import edit_config, reset, dashboard, edit_reporter, delete_reporter, edit_location, delete_location, edit_report, view_submissions, toggle_approval
from kit.excel.export.views import export_submissions, export_responses, export_approved_submissions
from kit.models import Report, Indicator
from kit.util import get_xform_list, get_xformfield_list
from rapidsms.contrib.locations.models import Location
from rapidsms.models import Contact
from rapidsms_xforms.models import XForm
from rapidsms_xforms.urls import urlpatterns as xform_urls
from rapidsms_httprouter.urls import urlpatterns as router_urls
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    # RapidSMS core URLs
    (r'^account/', include('rapidsms.urls.login_logout')),
    url(r'^$', dashboard, name='rapidsms-dashboard'),
    url('^accounts/login', 'rapidsms.views.login'),
    url('^accounts/logout', 'rapidsms.views.logout'),

    url('^config/$', edit_config),
    url('^config/reset/$', reset),
    url('^config/locations/$', bulk_upload, { \
        'model':Location, \
        'template':'/static/kit/spreadsheets/locations_tmpl.xls', \
        'redirect_url':'/', \
    }, name='upload-locations'),
    url('^config/users/$', bulk_upload, { \
        'model':Contact, \
        'model_name':'User', \
        'template':'/static/kit/spreadsheets/users_tmpl.xls', \
        'redirect_url':'/', \
    }, name='upload-contacts'),
    url('^config/reports/$', bulk_upload, { \
        'model':Report, \
        'model_name':'Report', \
        'template':'/static/kit/spreadsheets/reports_tmpl.xls', \
        'html_template':'kit/upload_indicators.html', \
        'redirect_url':'/', \
    }, name='upload-reports'),
    url('^config/indicators/$', bulk_upload, { \
        'model':Indicator, \
        'model_name':'Indicator', \
        'template':'/static/kit/spreadsheets/indicators_tmpl.xls', \
        'redirect_url':'/', \
    }, name='upload-indicators'),

    url('^users/$', generic, { \
        'model':Contact, \
        'results_title':'Users', \
        'action_forms':[MassTextForm, AssignGroupForm], \
        'base_template':'kit/contacts_base.html',
        'partial_row':'kit/partials/contacts/contacts_row.html', \
        'columns':[ \
            ('Name', True, 'name', SimpleSorter()), \
            ('Number', True, 'connection__identity', SimpleSorter(),), \
            ('Location', True, 'reporting_location__name', SimpleSorter(),), \
            ('Role(s)', True, 'groups__name', SimpleSorter()), \
            ('', False, '', None)],
    }, name="kit-users"),
    url(r'^user/(?P<contact_pk>\d+)/edit', edit_reporter),
    url(r'^user/(?P<contact_pk>\d+)/delete', delete_reporter),
    url(r'^user/(?P<pk>\d+)/show', generic_row, {'model':Contact, 'partial_row':'kit/partials/contacts/contacts_row.html'}),

    url('^locations/$', generic, { \
        'model':Location, \
        'results_title':'Locations', \
        'base_template':'kit/locations_base.html',
        'partial_row':'kit/partials/locations/locations_row.html', \
        'columns':[ \
            ('Name', True, 'name', SimpleSorter()), \
            ('Type', True, 'type__name', SimpleSorter(),), \
            ('Parent', True, 'tree_parent__name', SimpleSorter(),), \
            ('', False, '', None)],
    }, name="kit-locations"),
    url(r'^location/(?P<location_pk>\d+)/edit', edit_location),
    url(r'^location/(?P<location_pk>\d+)/delete', delete_location),
    url(r'^location/(?P<pk>\d+)/show', generic_row, {'model':Location, 'partial_row':'kit/partials/locations/locations_row.html'}),

    url('^reports/$', generic, { \
        'model':Report, \
        'queryset': get_xform_list, \
        'results_title':'Reports', \
        'base_template':'kit/reports_base.html',
        'partial_row':'kit/partials/reports/reports_row.html', \
        'columns':[ \
            ('Report', True, 'name', SimpleSorter()), \
            ('Indicators', False, 'fields', None,), \
            ('SMS Keyword', True, 'keyword', SimpleSorter(),), \
            ('', False, '', None)],
    }, name="kit-reports"),
    url("^reports/(?P<xform_pk>\d+)/export/$", export_submissions),
    url("^reports/(?P<xform_pk>\d+)/export_approved/$", export_approved_submissions),
    url("^reports/submissions/(?P<submission_id>\d+)/edit/", edit_report),
    url("^reports/submissions/(?P<submission_id>\d+)/tgapprove/", toggle_approval),
    url("^reports/(?P<xform_pk>\d+)/view/$", view_submissions),

    url("^responses/(?P<poll_pk>\d+)/export/$", export_responses),

    url('^indicators/$', generic, { \
        'model':Indicator, \
        'queryset': get_xformfield_list, \
        'results_title':'Active Indicators', \
        'base_template':'kit/indicators_base.html',
        'partial_row':'kit/partials/indicators/indicators_row.html', \
        'selectable':False, \
        'columns':[ \
            ('Report', True, 'xform__name', SimpleSorter()), \
            ('Name', True, 'name', SimpleSorter()), \
            ('Type', False, 'type', None,), \
            ('SMS Keyword', True, 'command', SimpleSorter(),), ],
    }, name="kit-indicators"),

    # RapidSMS contrib app URLs
    (r'^ajax/', include('rapidsms.contrib.ajax.urls')),
    (r'^export/', include('rapidsms.contrib.export.urls')),
    (r'^httptester/', include('rapidsms.contrib.httptester.urls')),
    (r'^locations/', include('rapidsms.contrib.locations.urls')),
    (r'^messaging/', include('rapidsms.contrib.messaging.urls')),
    (r'^scheduler/', include('rapidsms.contrib.scheduler.urls')),
    (r'^polls/', include('poll.urls')),
) + xform_urls + contact_urls + router_urls

if settings.DEBUG:
    urlpatterns += patterns('',
        # helper URLs file that automatically serves the 'static' folder in
        # INSTALLED_APPS via the Django static media server (NOT for use in
        # production)
        (r'^', include('rapidsms.urls.static_media')),
    )

#from rapidsms_httprouter.router import get_router
#get_router(start_workers=True)

