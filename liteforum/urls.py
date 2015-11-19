from django.conf.urls import include, url
from django.contrib import admin

import user
from topic.views import home, topic, node, node_list, new_post, test

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    # url(r'^member/(?P<username>[A-Za-z0-9]+)$', views.member, name='member'),
    url(r'^t/(?P<topic_id>\d+)/$', topic, name='topic'),
    url(r'^node/(?P<nodename>[A-Za-z0-9]+)$', node, name='node'),
    url(r'^nodes$', node_list, name='node_list'),
    url(r'^new$', new_post, name='new_post'),

    url(r'^accounts/login$', user.views.login),
    url(r'^accounts/logout$', user.views.logout),
    url(r'^accounts/register$', user.views.register),
    url(r'^accounts/profile$', user.views.profile),
    url(r'^accounts/profile/edit$', user.views.profile_edit),
    url(r'^accounts/restore$', user.views.restore),
    url(r'^test$', test)
]
