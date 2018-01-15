from .views import BlogRudView

from django.conf.urls import url, include

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogRudView.as_view(), name='blog-rud')
]
