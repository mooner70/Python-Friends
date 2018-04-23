from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^main$', views.main),
    url(r'^loggedin$', views.loggedin),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^user/(?P<id>\d+)$', views.user),
    url(r'^friends$', views.friends),
    url(r'^add/user/friends/(?P<id>\d+)$', views.add_to_list),
    url(r'^remove/user/friends/(?P<id>\d+)$', views.remove_from_list),
]