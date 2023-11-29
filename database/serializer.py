from rest_framework import serializers
from .models import Works

class works_serializers(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = "__all__"