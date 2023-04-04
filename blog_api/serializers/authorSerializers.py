from rest_framework import serializers
from blog_api.models.author import Author
from blog_api.serializers.blogSerializers import BlogSerializer

class AuthorSerializer(serializers.ModelSerializer):
    blog = BlogSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields =  ['id', 'name', 'blog']