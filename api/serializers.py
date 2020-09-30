from rest_framework import serializers

from api.models import Manufacturer, ShoeType, ShoeColor, Shoe

# Got help from Matthew Perry in that he suggested I start after creating the models by making the serializers and then views next.
class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = [
            'id',
            'name',
            'website'
        ]

class ShoeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeType
        fields = [
            'id',
            'style'
        ]

class ShoeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = [
            'id',
            'color_name'
        ]

class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = [
            'id',
            'size',
            'brand_name',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type'
        ]