from django.conf.urls import url 
from technicians import views 
 
urlpatterns = [ 
    url(r'^$', views.technician_list),
    url(r'^(?P<pk>[0-9]+)$', views.technician_detail)
]
