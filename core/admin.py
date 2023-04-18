from django.contrib import admin
from .models import Region,SubRegion,ProductCategories,Attribute,Unit,Quantity,Diet,ProductImage,Product,ProductRegion
from django.shortcuts import get_object_or_404 ,redirect
from django.http import request
from django.utils.html import format_html
from django.urls import reverse
from django import forms
from django.forms import ModelForm,CheckboxSelectMultiple
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.urls import path
from django.template.loader import get_template
from fieldsets_with_inlines import FieldsetsInlineMixin
from django.contrib.postgres.fields import ArrayField

# Register your models here.
admin.site.register(ProductCategories)
admin.site.register(Attribute)
admin.site.register(Unit)
admin.site.register(Quantity)
admin.site.register(Diet)
admin.site.register(SubRegion)
admin.site.register(Region)


class ProductRegionInlineForm(forms.ModelForm):
    
    class Meta:       
        widgets = {
            'subregion': forms.CheckboxSelectMultiple,
        }
    
    
class ProductRegionInline(admin.TabularInline):
    
    extra = 0
    model = ProductRegion
    form=ProductRegionInlineForm
    
    

        
class ProductImageInline(admin.TabularInline):
    model = ProductImage   
    # insert_before = 'attribute'
    extra = 1
    
    
class ProductForm(forms.ModelForm):   
     
    class Media:
        js = (
            'https://code.jquery.com/jquery-3.6.0.min.js',  # add jQuery
        )
    class Meta:
       
        widgets = {
            'attribute': forms.CheckboxSelectMultiple,
        }

        
        
class ProductAdmin(FieldsetsInlineMixin,admin.ModelAdmin):
    def get_regions(self,obj):
        return "\n".join([p.subregion for p in obj.subregion.all()])
     
    list_display=["Productname","total_price","product_status","get_regions"]         
    inlines = [ProductImageInline,ProductRegionInline] 
    readonly_fields = ["total_price",] 
    filter_horizontal = ('attribute',)    
    form=ProductForm   
    fieldsets_with_inlines = (
        ("Product", {
            'fields': ('Productname','Description','position'),
        }),(ProductRegionInline),(ProductImageInline),
            
       
        (None, {
            'fields': (('attribute','diet'),('is_deleted','is_favorite','available_now'),'discount_type','discount','price',('packing_charge','commission'),'total_price'),
        }),
    )
    
    
   
    
    
    
    
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     # Prefetch the related regions and subregions to reduce database queries
    #     qs = qs.prefetch_related('region', 'subregion')
    #     return qs

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == 'subregion':
            # Limit the subregion choices to those belonging to the selected region(s)
            # region_ids = request.GET.getlist('region')
            # kwargs['queryset'] =SubRegion.objects.all()
        #     if region_ids:
        #         kwargs['queryset'] = SubRegion.objects.filter(region_id=region_ids)
                
        #     else:
        #         kwargs['queryset'] = SubRegion.objects.all()
        # return super().formfield_for_manytomany(db_field, request, **kwargs)
   
        
    # class Media:
    #     js = ['core/js/product_admin.js']   
admin.site.register(Product, ProductAdmin)
