from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^add_page/(?P<category_name_slug>[\w\-]+)/$', views.add_page, name='add_page'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^page/(?P<page_slug>[\w\-]+)/$', views.page, name='page'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^add_profile/', views.register_profile, name='register_profile'),
        url(r'^profile/', views.profile, name='profile'),
        # url(r'^search/', views.search, name='search'),

)