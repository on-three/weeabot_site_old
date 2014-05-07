# vim: set ts=2 expandtab:
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
  url(r'^$', 'jisho.views.home', name='home'),
  url(r'^vocab/$', 'jisho.views.VocabularyListsView', name='VocabularyListsView'),
  url(r'^vocab/(?P<listname>\w+)', 'jisho.views.VocabularyListsView', name='VocabularyListView'),
  url(r'^nick/(?P<nick>\w+)', 'jisho.views.NickView', name='NickView'),
)


