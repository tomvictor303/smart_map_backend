from django.conf.urls import url 
from datasets import views 
 
urlpatterns = [ 
    url(r'^tasks$', views.task_list),
    # url(r'^(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^published$', views.tutorial_list_published)
]
