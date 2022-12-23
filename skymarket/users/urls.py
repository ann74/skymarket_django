from django.urls import path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig


app_name = UsersConfig.name

users_router = SimpleRouter()
users_router.register("users", UserViewSet, basename="users")

urlpatterns = [

]

urlpatterns += users_router.urls
