from home.models import*
from rest_framework import serializers

class productserializer (serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name','slug','description','price','image','category','seller')


class product2serializer (serializers.ModelSerializer):
    class Meta:
        model = product2
        fields = ('product','manufacturer_name','current_location','origin_country','date_added')
 