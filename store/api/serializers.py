from rest_framework import serializers
from store.models import Category, Book, Order, Discount_copon, payment,  refund

class Category_serializer (serializers.ModelSerializer) :
    class Meta : 
        model = Category
        fields = '__all__'

class Products_serializer (serializers.ModelSerializer) :
    class Meta : 
        model = Book
        fields = '__all__'

class Order_serializer (serializers.ModelSerializer) :
    class Meta : 
        model = Order
        fields = '__all__'

class discount_copon_serializer (serializers.ModelSerializer) :
    class Meta : 
        model = Discount_copon
        fields = '__all__'    

class payment_serializer (serializers.ModelSerializer) :
    class Meta : 
        model = payment
        fields = '__all__'  

class refund_serializer (serializers.ModelSerializer) :
    class Meta : 
        model = refund
        fields = '__all__'         

                  