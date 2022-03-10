from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework.views import APIView
from rest_framework .response import Response
from rest_framework import status
from rest_framework import  permissions

from .models import Article
from .serializers import ArticleSerializer
from rest_framework.permissions import IsAdminUser
# Create your views here.

class ArticleAPIView(APIView):
    # nếu bất kì ai cũng call được thì bỏ 16
    #nếu có token mới code được thì để dòng 16
    permission_classes = [IsAdminUser]
    
    def get(self , request):
        
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many= True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ArticleSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):
    def get_object(self , id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return HttpResponse(status= status.HTTP_404_NOT_FOUND)
    def get(self , request , id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    def put(self , request , id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article , data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    def detele(self , request , id):
        
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)      

