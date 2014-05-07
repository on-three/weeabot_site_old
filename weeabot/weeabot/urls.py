from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'weeabot.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),

  url(r'^$', TemplateView.as_view(template_name='weeabot/index.html'),
    name='home'),
  url(r'^jisho/', include('jisho.urls')),
  url(r'^accounts/profile/', TemplateView.as_view(template_name='weeabot/profile.html')),
  url(r'^accounts/', include('allauth.urls')),
  url(r'^admin/', include(admin.site.urls)),
)
