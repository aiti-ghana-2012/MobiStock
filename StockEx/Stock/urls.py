from django.conf.urls.defaults import *
import views

#urlpatterns = patterns('',
#	url(r'^list/$', views.notes_list, name='notes_list'),
#	url(r'^detail/(?P<id>\d+)/$', views.notes_detail, name='notes_detail'),
#)
urlpatterns = patterns('',
    url(r'^$', 'Stock.views.home'),
    url(r'^asset/$', 'Stock.views.assets_list'),
    url(r'^json/companies/$', 'Stock.views.json_companies'),
    url(r'^json/index/$', 'Stock.views.json_index'),
    url(r'^about/$', 'Stock.views.about_us'),
    url(r'^eureka/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'Stock.views.post_detail'),
    url(r'^eureka/search/(?P<term>.*?)$','Stock.views.post_search'),
    url(r'^comments/(?P<id>\d+)/edit/$','Stock.views.edit_comment'),
    # News urls
    url(r'^news/(\d{4})/$', 'Stock.views.year_archive'),

)
