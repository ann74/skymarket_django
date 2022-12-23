from django.urls import path
from rest_framework import routers

from ads.apps import SalesConfig
from ads.views import AdViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register("ads", AdViewSet)

app_name = SalesConfig.name

urlpatterns = [
    path('<int:ad_pk>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:ad_pk>/comments/<int:pk>/', CommentViewSet.as_view({"get": "retrieve", 'patch': 'update', 'delete': 'destroy'}))
]

urlpatterns += router.urls
