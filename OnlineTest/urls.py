from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OnlineTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^dashboard/(?P<pid>\d+)$', 'MCQTest.views.home_view', name='Home page'),
    url(r'^login/$', 'MCQTest.views.loginview', name='Login page'),
    url(r'^register/$', 'MCQTest.views.register_view', name='Register page'),
    url(r'^dashboard/$', 'MCQTest.views.dashboard_view', name='Dashboard page'),
    url(r'^practice/(?P<pid>\d+)$', 'MCQTest.views.practice_view', name='Practice page'),
    
    # logout
    url(r'^logout/$', 'MCQTest.views.logout_view', name='Logout'),

    # reset Password
    url(r'^reset/$', 'MCQTest.views.reset_view', name='reset password'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$','MCQTest.views.reset_confirm', name='password_reset_confirm'),
    url(r'^$', 'MCQTest.views.reset', name='reset'),
    url(r'^success/$', 'MCQTest.views.success', name='success'),

)
