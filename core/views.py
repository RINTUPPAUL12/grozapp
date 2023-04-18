# from django.shortcuts import render
from django.http import JsonResponse

from .models import ProductCategories,SubRegion, Region,Product
from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status 
from .serializers import ProductCategoriesSerializer 
# Create your views here.
import json        
  
class ProductCategoriesView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = ProductCategories.objects.all()  
        serializers = ProductCategoriesSerializer(result, many=True).data
        # data = ProductCategoriesSerializer(ProductCategories.objects.all(), many=True).data        
        # json_data = JSONRenderer().render(data)
        json_data= json.dumps(serializers)
        print(json_data)        
        with open('my_data.json', 'w') as f:
            f.write(json_data)
        return Response({'status': 'success', "productCategories":serializers}, status=200)  
  
    def post(self, request):  
        serializer = ProductCategoriesSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
