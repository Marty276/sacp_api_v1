from django.urls import path, include
from .views import Works_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"works", Works_views, "works")

urlpatterns = [
    path("api/", include(router.urls))
]