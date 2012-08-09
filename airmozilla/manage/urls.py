from django.conf.urls.defaults import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^/?$', views.dashboard, name='home'),
    url(r'^users/(?P<id>\d+)/$', views.user_edit, name='user_edit'),
    url(r'^users/', views.users, name='users'),
    url(r'^groups/(?P<id>\d+)/$', views.group_edit, name='group_edit'),
    url(r'^groups/remove/(?P<id>\d+)/$', views.group_remove,
                                         name='group_remove'),
    url(r'^groups/new/$', views.group_new, name='group_new'),
    url(r'^groups/$', views.groups, name='groups'),
    url(r'^events/request/$', views.event_request, name='event_request'),
    url(r'^events/(?P<id>\d+)/$', views.event_edit, name='event_edit'),
    url(r'^events/archive/(?P<id>\d+)/$', views.event_archive,
                                          name='event_archive'),
    url(r'^events/duplicate/(?P<copy_id>\d+)/$', views.event_duplicate,
                                            name='event_duplicate'),
    url(r'^events/remove/(?P<id>\d+)/$', views.event_remove,
                                         name='event_remove'),
    url(r'^events/$', views.events, name='events'),
    url(r'^tag-autocomplete/$', views.tag_autocomplete,
                                name='tag_autocomplete'),
    url(r'^participant-autocomplete/$', views.participant_autocomplete,
                                        name='participant_autocomplete'),
    url(r'^participants/new/$', views.participant_new, name='participant_new'),
    url(r'^participants/(?P<id>\d+)/$', views.participant_edit,
                                       name='participant_edit'),
    url(r'^participants/remove/(?P<id>\d+)/$', views.participant_remove,
                                               name='participant_remove'),
    url(r'^participants/email/(?P<id>\d+)/$', views.participant_email,
                                              name='participant_email'),
    url(r'^participants/$', views.participants, name='participants'),
    url(r'^categories/new/$', views.category_new, name='category_new'),
    url(r'^categories/(?P<id>\d+)/$', views.category_edit,
                                     name='category_edit'),
    url(r'^categories/remove/(?P<id>\d+)/$', views.category_remove,
                                            name='category_remove'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^templates/env-autofill/$', views.template_env_autofill,
                                      name='template_env_autofill'),
    url(r'^templates/new/$', views.template_new, name='template_new'),
    url(r'^templates/(?P<id>\d+)/$', views.template_edit,
                                     name='template_edit'),
    url(r'^templates/remove/(?P<id>\d+)/$', views.template_remove,
                                            name='template_remove'),
    url(r'^templates/$', views.templates, name='templates'),
    url(r'^locations/new/$', views.location_new, name='location_new'),
    url(r'^locations/(?P<id>\d+)/$', views.location_edit,
                                     name='location_edit'),
    url(r'^locations/remove/(?P<id>\d+)/$', views.location_remove,
                                            name='location_remove'),
    url(r'^locations/tz/$', views.location_timezone, name='location_timezone'),
    url(r'^locations/$', views.locations, name='locations'),
    url(r'^approvals/$', views.approvals, name='approvals'),
    url(r'^approvals/(?P<id>\d+)/$', views.approval_review,
                                     name='approval_review')
)
