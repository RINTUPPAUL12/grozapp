from rest_framework import serializers  
from .models import ProductCategories
from rest_framework.renderers import JSONRenderer
  
class ProductCategoriesSerializer(serializers.ModelSerializer): 
    
    productCategories = serializers.CharField(max_length=50)
    icon = serializers.ImageField()
    image = serializers.ImageField()
    position = serializers.IntegerField(default=1)
    is_active = serializers.BooleanField(default=True)
    
    def create(self, validated_data):  
        """ 
        Create and return a new `ProductCategories` instance, given the validated data. 
        """  
        return ProductCategories.objects.create(**validated_data)  
  
    def update(self, instance, validated_data):  
        """ 
        Update and return an existing `productCategories` instance, given the validated data. 
        """  
        instance.productCategories = validated_data.get('productCategories', instance.productCategories)  
        instance.icon = validated_data.get('icon', instance.icon)  
        instance.image = validated_data.get('image', instance.address)  
        instance.position = validated_data.get('position', instance.position)  
        instance.is_active = validated_data.get('is_active', instance.is_active)  
  
        instance.save()  
        return instance 

  
    class Meta:  
        model = ProductCategories  
        fields = ('__all__')  
        


# with open("my_data.json", "w") as f:
#     json.dump(json_data, f)   