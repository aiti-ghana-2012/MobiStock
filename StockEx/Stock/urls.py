from django.conf.urls.defaults import *
import views

#urlpatterns = patterns('',
#	url(r'^list/$', views.notes_list, name='notes_list'),
#	url(r'^detail/(?P<id>\d+)/$', views.notes_detail, name='notes_detail'),
#)
urlpatterns = patterns('',
    url(r'^$', 'blog.views.home'),
    url(r'^posts/$', 'blog.views.post_list'),
    url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$',           'blog.views.post_detail'),
    url(r'^posts/search/(?P<term>.*?)$','blog.views.post_search'),
)
