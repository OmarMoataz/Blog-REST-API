from django.conf.urls import url
from .views import PersonAPIView, PersonRudView 

urlpatterns = [
    url(r'^(?P<pk>\d+)$', PersonRudView, name='person-rud'),
    url(r'^$', PersonAPIView.as_view(), name='person-create')
]
