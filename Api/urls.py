
from django.urls import path, include
from rest_framework import routers
from .views import CustomerViewSet



router = routers.DefaltRouter()
routers.register("customer", CustomerViewSet)

urlpatterns = [
    path("", include(router.urls)),
    ]