from rest_framework import serializers
from .models import Article
# class UserSerializers ( serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [ 'id' 'password', 'email' , 'username']
#         extra_kwargs={'password' :{ 'write_only': True} ,'id ' :{ 'read_only': True}}


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields= ['id','title','author' ]
        # fields ='__all__'