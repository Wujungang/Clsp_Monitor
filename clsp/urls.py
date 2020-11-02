from django.conf.urls import url
from clsp.views import *

urlpatterns = [
    url(r'^$',index),
    url(r'^middleware$',middleware),
    url(r'^register/$',RegisterView.as_view(),name='register'),
    url(r'^login/$',AuthView.as_view(),name='register1')
]