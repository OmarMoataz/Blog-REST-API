from django.conf.urls import url
from .views import CommentAPIView, CommentRudView

urlpatterns = [
    url(r'^(?P<pk>\d+)$', CommentRudView, name='comment-rud'),
    url(r'^$', CommentAPIView.as_view(), name='comment-create')
]
