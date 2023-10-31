from django.conf.urls import url 
from plans import views 
 
urlpatterns = [ 
    url(r'^$', views.plan_list),
    url(r'^smart_delete$', views.plan_smart_delete),
    # url(r'^priority$', views.tutorial_list),
]
