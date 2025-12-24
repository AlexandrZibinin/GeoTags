from rest_framework import generics

from geotags.models import Point
from geotags.serializer import PointSerializer


class PointCreateAPIView(generics.CreateAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

class PointListAPIView(generics.ListAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

class PointRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class PointUpdateAPIView(generics.UpdateAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class PointDeleteAPIView(generics.DestroyAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer