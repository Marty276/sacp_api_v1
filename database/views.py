from rest_framework import viewsets
from .serializer import requests_serializers, to_collect_serializers, to_pay_or_paid_serializers
from .models import Requests, To_Collect, To_Pay_Or_Paid

class Requests_views(viewsets.ModelViewSet):
    serializer_class = requests_serializers
    queryset = Requests.objects.all()

class To_Collect_views(viewsets.ModelViewSet):
    serializer_class = to_collect_serializers
    queryset = To_Collect.objects.all()

class To_Pay_or_Paid_views(viewsets.ModelViewSet):
    serializer_class = to_pay_or_paid_serializers
    queryset = To_Pay_Or_Paid.objects.all()
