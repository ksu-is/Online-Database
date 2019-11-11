"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # questionnaire urls
    url(r'q/', include('questionnaire.urls')),
    url(r'^take/(?P<questionnaire_id>[0-9]+)/$',
        'questionnaire.views.generate_run'),
    url(r'^$', 'questionnaire.page.views.page',
        {'page_to_render': 'index'}),
    url(r'^(?P<lang>..)/(?P<page_to_trans>.*)\.html$',
        'questionnaire.page.views.langpage'),
    url(r'^(?P<page_to_render>.*)\.html$',
        'questionnaire.page.views.page'),
    url(r'^setlang/$', 'questionnaire.views.set_language'),
]
