from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.course),
    url(r'^delete_course$', views.delete),
    url(r'^destroy/(?P<id>\d+)$', views.destroy)
    # url(r'^delete_course/(?P<id>\d+)$', views.delete)
]
