from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import terrorism_info

urlpatterns = [
    url(r'terrorism/(?P<id>[0-9]+)/$', terrorism_info),
]

urlpatterns = format_suffix_patterns(urlpatterns)
