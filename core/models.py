from django.db import models
from django.core.exceptions import ValidationError
from compositefk.fields import CompositeForeignKey
from django.conf import global_settings
from django.utils import translation
# from smart_selects.db_fields import GroupedForeignKey
# Create your models here.

class ProductCategories(models.Model):
    """
    Model for Product Categories
    """
    productCategories = models.CharField(max_length=50, unique=True)
    icon = models.ImageField(upload_to='product_type_icon')
    image = models.ImageField(upload_to='product_type')
    position = models.SmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.productCategories
    
class Attribute(models.Model):
    product_Category = models.ForeignKey(ProductCategories,on_delete=models.CASCADE,related_name="attribute_product_categories" )
    attribute = models.CharField(max_length=30, unique=True)
   
    def __str__(self):
        return self.attribute
    


class Unit(models.Model):
    """
    Model for units
    """
    name = models.CharField(max_length=15, unique=True)

    class Meta:
        verbose_name = "Unit"
        verbose_name_plural = "Units"
    
    def __str__(self):
        return self.name
    
class Quantity(models.Model):
    """Model for quantity."""
    quantity = models.CharField(max_length=30, unique=True)
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE,related_name='quantity_unit')

    class Meta:
        verbose_name = "Quantity"
        verbose_name_plural = "Quantities"

    def __str__(self):
        return self.quantity
    
   
class Diet(models.Model):
    """Model for diet."""
    diet = models.CharField(max_length=200, unique=True)
    # unit = models.ForeignKey(Unit,on_delete=models.CASCADE,related_name='quantity_unit')

    class Meta:
        verbose_name = "diet"
        verbose_name_plural = "diets"

    def __str__(self):
        return self.diet

               
               

class Region(models.Model):
    """
    Model for Region
    """
    Region = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"
        db_table = "Region"
        
    
    def __str__(self):
        return self.Region



   
def validate_coordinates(values):
    is_exception = False
    if not isinstance(values, list):
        is_exception = True
    else:
        is_exception = not all([isinstance(value, list) and len(value)==2 
                            and all([isinstance(item, int) or
                            isinstance(item, float)
                             for item in value]) for value in values])
    if is_exception:
        raise ValidationError("Value for 'coordinates' accepts only list of coordinates\
                              example : [[436.3549,10.1141],[436.3658638,10.110]]")


class SubRegion(models.Model):
    """
    Model for SubRegions
    """ 
    Region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    SubRegion = models.CharField(max_length=15, unique=True)
    coordinates = models.JSONField(validators =[validate_coordinates],null=True)

    class Meta:
        verbose_name = "SubRegion"
        verbose_name_plural = "SubRegions"
        db_table = "SubRegions"
    
    def __str__(self):
        return self.SubRegion  
    




class Product(models.Model):   
       
    Productname = models.CharField(max_length=200)     
    Description = models.TextField()    
    position = models.PositiveIntegerField(default=1)
    region= models.CharField(max_length=50, blank=True, null=True)
    # regio = models.ForeignKey(Region,null=True,on_delete=models.CASCADE,default=1) 
       
    subregion = models.ManyToManyField(SubRegion)
    
    # def subregionfilter(self,request):
    #     selected_region_id = request.POST.get('Region')
    #     # SubRegion = SubRegion.objects.create(Region_id=selected_region_id)
    # Subregion = models.ForeignKey(SubRegion,on_delete=models.CASCADE)
        
    # models.ForeignKey(SubRegion, on_delete=models.CASCADE,null=False, blank=False,limit_choices_to={'Region': Region})
    
    attribute = models.ManyToManyField(
        Attribute,
        blank=True,
        related_name='product_attributes')
    
    diet = models.ForeignKey(Diet,on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    available_now = models.BooleanField(default=True)
    
    PRICE = "PRICE"
    PERCENTAGE = "PERCENTAGE"    
    DISCOUNT_CHOICES = ((PRICE, 'Price'),
                        (PERCENTAGE, 'Percentage'),
                        )     
    discount_type = models.CharField(max_length=10,choices=DISCOUNT_CHOICES,blank=True,null=True )
    discount = models.FloatField(default=0.0, blank=True, null=True)
        
    price = models.FloatField(default=0.0)    
    packing_charge = models.FloatField(default=0.0)
    commission = models.FloatField(default=0.0)
    
    # def total_price(self, obj):
    #     if self.discount_type == self.PRICE:
    #         return obj.price + obj.commission + obj.packing_charge - obj.discount
    #     elif self.discount_type == self.PERCENTAGE:
    #         return round(obj.price +obj.commission +obj.packing_charge - (obj.price*obj.discount/100),0)            
    #     else:
    #         return obj.price
    total_price=models.IntegerField()
    
    def total_price(self):
        if self.discount_type == self.PRICE:
            return self.price + self.commission + self.packing_charge - self.discount
        elif self.discount_type == self.PERCENTAGE:
            return round(self.price +self.commission +self.packing_charge - (self.price*self.discount/100),0)            
        else:
            return self.price
    
        
    
    def product_status(self):
        if self.available_now:
            return "In stock"
        else:
            return "Out of stock"
        
    def __str__(self):
        return self.Productname
        
    # def __str__(self):
    #     return f"{self.product_status}",{self.total_price}
        
        # return f"{self.product_status}, Rs{self.total_price()}, {self.Productname}"
    
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images',on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=1)
    # primary_key = True if you do not want to use default field "id" given by django to your model
    image = models.ImageField(upload_to='products',blank=True,null=True)
class ProductRegion(models.Model):
        # position = models.PositiveIntegerField(default=1)
        product = models.ForeignKey(Product, related_name='egion',on_delete=models.CASCADE)
        region=models.ForeignKey(Region,on_delete=models.CASCADE,default=1)#region = models.ManyToOneRel(Region)
        
        subregion = models.ManyToManyField(SubRegion) 
        # def get_regions(self):
        #     return "\n".join([p.regions for p in self.subregion.all()])
        # subregion = CompositeForeignKey(SubRegion, on_delete=models.CASCADE, to_fields={
        # "re_id": "customer_id",
        # "company": LocalFieldValue("company"),
        # "type_tiers": RawFieldValue("C")
    # })
        def __str__(self):
            return f""

