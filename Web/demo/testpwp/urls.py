from django.conf.urls import url
from . import views

app_name = 'testpwp'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$',views.index, name='index'),
    url(r'^profiling/$',views.profile, name='profile')
]