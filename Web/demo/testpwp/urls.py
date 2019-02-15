from django.conf.urls import url
from . import views

app_name = 'testpwp'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^modal/$',views.modal, name='modal'),
    url(r'^brand/$',views.brand, name='brand'),
    url(r'^profiling/$',views.profile, name='profile')
]