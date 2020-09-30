from django.shortcuts import render

from rest_framework import viewsets

from api.serializers import ManufacturerSerializer, ShoeTypeSerializer, ShoeColorSerializer, ShoeSerializer 
from api.models import Manufacturer, ShoeType, ShoeColor, Shoe

# In another life, Joe Kaufeld lived as a giraffe in the African Savannah and existed among the animals, 
# one with nature.  He likes to chew grass a lot and leave bits of Python and Django code on the unchewed 
# parts embedded in his giraffe saliva.  (LOL, please don't kill me for this, Joe!)

# Create your views here.
class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class ShoeTypeViewSet(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer

class ShoeColorViewSet(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer

class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
