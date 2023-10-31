from django.conf.urls import url, include 
from django.contrib import admin

urlpatterns = [ 
  # url(r'^admin/', admin.site.urls),
  url(r'^api/tutorials/', include('tutorials.urls')),
  url(r'^api/datasets/', include('datasets.urls')),
  url(r'^api/plans/', include('plans.urls')),
]
