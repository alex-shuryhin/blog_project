from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from blog import views

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request):
        return '/blog/add_profile/'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
        #Add in this url pattern to override the default pattern in accounts.
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/password/change/done/$', views.index, name='auth_password_change_done'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)