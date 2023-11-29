from rest_framework import viewsets
from .models import Works
from .serializer import works_serializers


class Works_views(viewsets.ModelViewSet):
    serializer_class = works_serializers
    queryset = Works.objects.all()