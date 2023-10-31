from django.conf.urls import url 
from tutorials import views 
 
urlpatterns = [ 
    url(r'^$', views.tutorial_list),
    url(r'^(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^published$', views.tutorial_list_published)
]
