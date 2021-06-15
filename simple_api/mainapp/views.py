from rest_framework import viewsets
from .serializers import POISerializer
from .models import POI

class POIView(viewsets.ModelViewSet):
    queryset = POI.objects.all()
    serializer_class = POISerializer
