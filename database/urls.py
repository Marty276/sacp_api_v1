from django.urls import path, include
from .views import Requests_views, To_Collect_views, To_Pay_or_Paid_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"requests", Requests_views, "requests")
router.register(r"to_collect", To_Collect_views, "to_collect")
router.register(r"to_pay_or_paid", To_Pay_or_Paid_views, "to_pay_or_paid")

urlpatterns = [
    path("api/", include(router.urls))
]