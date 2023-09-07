from rest_framework import serializers
from .models import Requests, To_Collect, To_Pay_Or_Paid

class requests_serializers(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = "__all__"

class to_collect_serializers(serializers.ModelSerializer):
    class Meta:
        model = To_Collect
        fields = "__all__"

class to_pay_or_paid_serializers(serializers.ModelSerializer):
    class Meta:
        model = To_Pay_Or_Paid
        fields = "__all__"