"""
HackerPack URL Configuration
"""
from django.conf.urls import url, include

urlpatterns = [
	url(r'', include('src.urls')),
]
