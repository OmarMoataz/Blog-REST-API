from .views import BlogRudView, BlogAPIView

from django.conf.urls import url, include

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogRudView.as_view(), name='blog-rud'),
    url(r'^$', BlogAPIView.as_view(), name='blog-create')
]
