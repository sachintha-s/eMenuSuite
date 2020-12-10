from rest_framework import serializers
from e_menu_api.models import Restaurant, Item, Order


class RestaurantSerializer(serializers.ModelSerializer):

    name = serializers.CharField()
    tip = serializers.FloatField()
    tax = serializers.FloatField()
    stripeid = serializers.CharField()
    password = serializers.CharField()
    currency = serializers.CharField()
    taxed = serializers.FloatField()
    lastTaxedReset = serializers.DateTimeField()
    lastTipReset = serializers.DateTimeField()
    menuurl = serializers.URLField()

    class Meta:
        model = Restaurant
        fields = ('name', 'tip', 'tax', 'stripeid', 'password', 'currency', 'taxed', 'lastTaxedReset', 'lastTipReset', 'menuurl')


class ItemSerializer(serializers.ModelSerializer):
    price = serializers.FloatField()
    item = serializers.CharField()
    req = serializers.BooleanField()

    class Meta:
        model = Item
        fields = ('restaurant', 'price', 'item', 'req')


class OrderSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField()
    chosen = serializers.BooleanField()
    cost = serializers.FloatField()
    items = serializers.CharField()
    notes = serializers.CharField(allow_blank=True, allow_null=True)
    phonenum = serializers.CharField()
    tablenum = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ('restaurant', 'time', 'chosen', 'cost', 'items', 'notes', 'phonenum', 'tablenum', 'tip', 'tax')
