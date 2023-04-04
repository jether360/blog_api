from rest_framework import serializers
from blog_api.models.blog import Blog


class BlogViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields =  ['id', 'blog','author']

#for author serializer
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields =  ['id', 'blog']